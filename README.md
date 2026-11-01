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

## John's Reviewr 0.5: YouTube e avaliações entre serviços

**Pesquisa:** em Dados → YouTube • API e conta Google, cadastre uma API Key do Google Cloud Console com YouTube Data API v3 habilitada. Em Buscar, selecione YouTube Music / vídeos. Resultados são vídeos, não faixas verificadas do catálogo YouTube Music. A opção Pesquisar diretamente no YouTube Music abre uma busca externa mesmo sem chave.

**Biblioteca parcial do YouTube:**
1. No Google Cloud, habilite YouTube Data API v3, configure a Tela de consentimento OAuth, escopo https://www.googleapis.com/auth/youtube.readonly e inclua a conta nos usuários de teste se necessário.
2. Crie credencial OAuth Android com o pacote com.sideb.musicratings e o SHA-1 do APK em configuracao-spotify.txt. O SHA-1 muda entre APKs debug assinados com chaves diferentes.
3. Crie também OAuth Client ID do tipo Aplicativo Web no mesmo projeto. Copie apenas o Client ID, não o Client Secret.
4. No app, em Dados → Configurar API e OAuth Google, informe API Key e OAuth Web Client ID. Se alterar este último depois de conectar, reinicie o app.
5. Conecte Google, autorize leitura e vá a Biblioteca → Playlists YouTube / Curtidas YouTube. A API não dá acesso a toda a biblioteca privada do YouTube Music.

**Notas entre plataformas:** use Vincular em vídeos ou faixas em reprodução. O app sugere correspondências conservadoras de título/artista, mas a associação só acontece após confirmação manual. Os vínculos são armazenados localmente e preservados no backup JSON.

**Importante:** links abrem o YouTube Music e podem exigir Play manual. O app não contorna Premium, DRM nem regras de fundo. Chaves de API em apps móveis podem ser extraídas; restrinja a API no Google Cloud, monitore cotas e não compartilhe segredos. Google pode exigir verificação de OAuth para distribuição pública.

**Atualização:** exporte JSON antes de desinstalar builds debug anteriores; a assinatura pode mudar.