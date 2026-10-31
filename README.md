# John's Reviewr 0.4 🎵

Aplicativo Android em Flutter e Kotlin para avaliar músicas em **meias estrelas**, calcular notas médias por álbum e organizar sua biblioteca Spotify. Funciona com música atual do Spotify/YouTube Music, busca e reprodução de faixas e álbuns, importação/exportação JSON/CSV e armazenamento local. Sem servidor próprio.

## O que mudou na v0.4
- Nome exibido no aplicativo e launcher: **John's Reviewr**
- Ícone exclusivo **JR em vinil preto, verde e branco**, inclusive na barra superior
- **Spotify App Remote SDK 0.8.0** para tentar iniciar música ou álbum mesmo sem player Spotify Connect ativo
- **Fallback Web API** quando o App Remote não está disponível
- Biblioteca com playlists, álbuns salvos, curtidas e músicas avaliadas
- Avisos flutuantes com texto branco
- Compatibilidade de importação de backups anteriores do Side B

## Baixar APK

Abra a aba **Actions** e selecione a execução mais recente com ✅ Success. Em **Artifacts**, baixe **johns-reviewr-v0.4.0-android**, extraia **Johns-Reviewr-v0.4.0-debug.apk** e instale no Android.

**Antes de desinstalar o app anterior, exporte o backup JSON de suas avaliações.** Assinaturas debug geradas no GitHub Actions podem variar entre compilações e impedir uma atualização direta.

## Configuração Spotify (importante)

Para o Spotify App Remote iniciar reprodução sem player ativo, configure cada Spotify Client ID no Spotify Developer Dashboard com:

- Redirect URI: `sideb://callback`
- Android package: `com.sideb.musicratings`
- SHA-1 do APK: consulte o arquivo **configuracao-spotify.txt** incluído no mesmo artefato ZIP do GitHub Actions.
- Spotify instalado, atualizado e com usuário autenticado no celular; reprodução exige plano Premium nos cenários suportados.

O nome **John's Reviewr** é exibido no Android e no aplicativo. Os identificadores técnicos legados do package, redirect URI e preferências `sideb_*` permanecem deliberadamente para preservar as avaliações e o login existentes. É possível renomear a entrada do aplicativo também no Spotify Developer Dashboard, mas sem alterar o Client ID.

App Remote é um SDK Beta: o comportamento depende da versão do aplicativo Spotify, das permissões e do SHA-1 registrado. Se a conexão falhar, o aplicativo usa como alternativa a Web API, que requer um dispositivo Spotify Connect ativo.

O YouTube Music depende do sistema Android de sessões de mídia (é necessário conceder acesso às notificações); não oferece integração oficial de busca e reprodução equivalente.

## Código-fonte

O arquivo de código-fonte completo da versão 0.4 está disponível na conversa ChatGPT. A compilação deste repositório aplica alterações versionadas em `.github/patches/` sobre o ZIP-base, mantendo o histórico das versões anteriores.


## Erro: "Explicit user authorization is required" (0.4.1)

Esse erro é do **Spotify App Remote**: significa que o controle remoto ainda não foi autorizado para o aplicativo/usuário selecionados. Não é a mesma coisa que o erro de player ativo da Web API.

Na versão **John's Reviewr 0.4.1**, o login OAuth inclui o escopo `app-remote-control` e solicita consentimento novamente. Em **Dados > Sua conta Spotify**, use **Reautorizar reprodução**; permita o acesso quando o Spotify perguntar. O botão não apaga notas.

Confira no Spotify Developer Dashboard de **cada Client ID usado no celular**:
- Redirect URI exatamente `sideb://callback`
- Android package `com.sideb.musicratings`
- SHA-1 do APK **específico que você instalou**, informado no `configuracao-spotify.txt` do artefato.
- Conta Spotify Premium permitida em Development Mode, quando aplicável.

O SDK já usa `showAuthView(true)`; a nova versão adiciona a permissão também ao OAuth Web PKCE. A autorização depende do Spotify instalado e pode continuar falhando por configuração ou limitações do SDK/serviço. Se for o caso, o aplicativo informa o diagnóstico em português.

**Atualização de APK debug:** exporte suas notas (Dados > Exportar JSON) antes de desinstalar a versão anterior. APKs gerados em runners diferentes podem ter certificados debug distintos e exigirem reinstalação.
