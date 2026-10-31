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
