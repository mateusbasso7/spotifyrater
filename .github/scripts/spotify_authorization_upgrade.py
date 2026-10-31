#!/usr/bin/env python3
"""Aprimora a autorização Spotify do John's Reviewr 0.4.1 no build Flutter."""
from pathlib import Path
import re
import sys

root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('/tmp/sideb-build')
spotify = root / 'lib/src/spotify.dart'
main = root / 'lib/main.dart'
pubspec = root / 'pubspec.yaml'

s = spotify.read_text(encoding='utf-8')
old_scopes = "static const scopes = 'user-read-currently-playing user-read-playback-state user-modify-playback-state user-library-read playlist-read-private playlist-read-collaborative';"
new_scopes = "static const scopes = 'user-read-currently-playing user-read-playback-state user-modify-playback-state user-library-read playlist-read-private playlist-read-collaborative app-remote-control';"
assert s.count(old_scopes) == 1, 'Escopos OAuth não encontrados'
s = s.replace(old_scopes, new_scopes)
old_auth = "      'code_challenge_method': 'S256',\n"
new_auth = "      'show_dialog': 'true', // Pede novo consentimento para o controle remoto.\n" + old_auth
assert s.count(old_auth) == 1, 'Parâmetros PKCE não encontrados'
s = s.replace(old_auth, new_auth)
old_error = "    } catch (webError) {\n      throw StateError('Não foi possível iniciar no Spotify. App Remote: $remoteReason. '\n          'Fallback Web API: $webError. Confira o Spotify instalado e o SHA-1 '\n          'do APK no Spotify Developer Dashboard.');\n    }"
new_error = """    } catch (webError) {
      if (remoteReason.contains('Explicit user authorization') ||
          remoteReason.contains('UserNotAuthorized') ||
          remoteReason.contains('authorization is required')) {
        throw StateError('O Spotify ainda não autorizou o controle de reprodução. '
            'Em Dados > Sua conta Spotify, toque em Reautorizar reprodução, '
            'aceite a permissão solicitada e tente novamente. '
            'Se continuar, confira Client ID, SHA-1 e Redirect URI no Spotify Developer Dashboard.');
      }
      throw StateError('A reprodução não começou. Confira o Spotify instalado, '
          'sua conta Premium e a configuração do Client ID no Dashboard. '
          'Detalhes: $remoteReason / $webError');
    }"""
assert s.count(old_error) == 1, 'Tratamento de erro de reprodução não encontrado'
s = s.replace(old_error, new_error)
spotify.write_text(s, encoding='utf-8')

m = main.read_text(encoding='utf-8')
old_btn = """            const SizedBox(height: 7),
            SizedBox(width: double.infinity, child: OutlinedButton.icon(
              onPressed: _showSpotifyApps,
"""
new_btn = """            const SizedBox(height: 7),
            if (spotify.connected) ...[
              SizedBox(width: double.infinity, child: OutlinedButton.icon(
                onPressed: () async {
                  try {
                    await spotify.login();
                    _toast('Autorize o controle de reprodução na página do Spotify.');
                  } catch (e) { _toast('$e'); }
                },
                icon: const Icon(Icons.verified_user_outlined),
                label: const Text('Reautorizar reprodução'),
              )),
              const SizedBox(height: 7),
            ],
            SizedBox(width: double.infinity, child: OutlinedButton.icon(
              onPressed: _showSpotifyApps,
"""
assert m.count(old_btn) == 1, 'Painel da conta Spotify não encontrado'
m = m.replace(old_btn, new_btn)
assert 'v0.4.0' in m, 'Versão base não encontrada'
m = m.replace('v0.4.0', 'v0.4.1')
main.write_text(m, encoding='utf-8')

p = pubspec.read_text(encoding='utf-8')
p, count = re.subn(r'(?m)^version: .*$', 'version: 0.4.1+6', p)
assert count == 1, 'Versão pubspec não encontrada'
pubspec.write_text(p, encoding='utf-8')
assert 'app-remote-control' in spotify.read_text(encoding='utf-8')
assert 'Reautorizar reprodução' in main.read_text(encoding='utf-8')
print("John's Reviewr 0.4.1: permissão App Remote, reautorização explícita e erros legíveis configurados")
