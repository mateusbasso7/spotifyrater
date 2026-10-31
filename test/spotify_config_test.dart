import 'package:flutter_test/flutter_test.dart';
import 'package:musicratings/src/spotify.dart';

void main() {
  test('Client ID Spotify deve ter 32 caracteres hexadecimais', () {
    expect(SpotifyAppConfig.isValidClientId('a0df0a300a1d4905b6ceb08f996b56f3'), isTrue);
    expect(SpotifyAppConfig.isValidClientId('123'), isFalse);
    expect(SpotifyAppConfig.isValidClientId('z0df0a300a1d4905b6ceb08f996b56f3'), isFalse);
  });

  test('Cadastro local suporta apelido e serialização', () {
    const app = SpotifyAppConfig(label: 'Amigos', clientId: 'a0df0a300a1d4905b6ceb08f996b56f3');
    final copy = SpotifyAppConfig.fromJson(app.toJson());
    expect(copy.label, 'Amigos');
    expect(copy.clientId, app.clientId);
  });
}
