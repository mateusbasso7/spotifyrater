# Side B. — avaliador de músicas Android

Aplicativo Flutter para avaliar músicas com notas de **0,5 a 5 estrelas**, calcular médias por álbum, salvar avaliações localmente e exportar backups em JSON/CSV. Integração com Spotify via OAuth PKCE e tentativa de leitura do YouTube Music pelas sessões de mídia do Android.

## Gerar o APK pelo celular

1. Baixe o arquivo **sideb_flutter_id_atualizado.zip** disponibilizado na conversa do ChatGPT.
2. Neste repositório GitHub, use **Add file > Upload files** e envie o ZIP **sem extrair**, na raiz do repositório.
3. Confirme o upload com **Commit changes**.
4. Abra a aba **Actions** e escolha **Compilar APK Side B.**.
5. Quando a execução estiver concluída (verde), abra-a e baixe o artefato **sideb-android-apk**.
6. Extraia `app-debug.apk` do artefato ZIP e instale no Android.

A automação é acionada ao enviar o ZIP e também pode ser executada manualmente.

### Spotify

O Client ID público fornecido pelo desenvolvedor está no código. Configure a Redirect URI **sideb://callback** no Spotify Developer Dashboard. Nunca envie Client Secret nem senhas.

### Observações

- O APK é **debug**, destinado a testes.
- Não há backend nem banco de dados em nuvem.
- É necessário que o usuário autorize o Spotify e ative permissão especial no Android para leitura das sessões de mídia, se quiser integrar o YouTube Music.
- O YouTube Music pode limitar os dados exibidos e os controles.
- **Ainda não foi possível compilar nem testar o app**: o primeiro Actions confirmará a viabilidade do build.


## Vários Client IDs (versão 0.2)

A compilação aplica automaticamente a atualização do Side B para permitir **cadastrar, selecionar e excluir Client IDs** diretamente no celular, em **Dados > Gerenciar Client IDs** (também disponível na tela Agora). A lista fica salva localmente. Ao selecionar outro Client ID, o app encerra a autorização Spotify anterior e pede um novo login; **as notas não são apagadas**. Para trocar apenas de usuário Spotify, basta usar Desconectar / Conectar.

Cada Client ID deve ser configurado em seu próprio Spotify Developer Dashboard com a URI de redirecionamento `sideb://callback`. Client ID não é e-mail nem ID da pessoa. O app não altera limites de uso da API Spotify.

O ZIP `sideb_flutter_codigo_fonte.zip` na raiz contém o código-base; a compilação incorpora o suporte a múltiplos IDs por meio do patch versionado em `.github/patches/`, sem exigir outro upload.
