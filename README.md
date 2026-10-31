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

## Versão 0.3 — Biblioteca e reprodução por busca

A nova versão permite:

- Buscar músicas e álbuns no catálogo Spotify e iniciar a reprodução via API oficial.
- Abrir um álbum e avaliar as faixas uma a uma.
- Navegar pela **Sua Biblioteca** com filtros Playlists, Álbuns salvos, Curtidas e Avaliados.
- Paginar a biblioteca (20 itens por página), atualizar puxando para baixo e reproduzir álbuns, playlists e faixas.
- Mostrar avisos flutuantes com texto branco e contraste legível.

**Permissões novas:** `user-library-read`, `playlist-read-private` e `playlist-read-collaborative`. Desconecte e conecte sua conta Spotify após atualizar, autorizando o novo acesso.

**Reprodução:** funciona pelo Spotify Web API em uma conta Premium e em um dispositivo com Spotify ativo; quando não há dispositivo ativo, abra o Spotify e inicie uma música antes de repetir. O Side B não transmite áudio nem substitui o aplicativo Spotify. Em desenvolvimento, a leitura do conteúdo de playlists de terceiros é limitada pelas regras atuais da API.

**Atualização do APK debug:** builds diferentes do GitHub Actions podem ser assinados por certificados de teste diferentes. Exporte as avaliações em JSON antes de atualizar. Se o Android recusar uma instalação sobre a anterior, desinstalar a versão velha apagará os dados locais; faça backup e importe-o depois.

O GitHub Actions monta o código-base do ZIP e aplica os patches versionados em `.github/patches/`, incluindo a versão 0.3.


## Instalação da versão 0.3.1 e APK anterior

Para identificar a versão instalada, abra o Side B e veja o **v0.3.1 junto ao logotipo**, na barra superior. A navegação inferior deve conter **Agora / Biblioteca / Buscar / Dados**. Se aparecer **Álbuns** em vez de **Biblioteca**, a versão anterior está em execução.

O artefato correto do GitHub Actions se chama **sideb-v0.3.1-android**, com o arquivo **SideB-v0.3.1-debug.apk** e \`build-info.txt\`.

As compilações de teste no GitHub Actions usam chaves debug geradas no runner e podem ter **assinaturas diferentes**. Portanto, ao tentar instalar o novo APK sobre uma versão antiga, o Android pode rejeitar a atualização. **Antes de desinstalar qualquer versão, use Dados > Exportar JSON e guarde o backup fora do aparelho.** Só então desinstale a versão antiga, instale SideB-v0.3.1-debug.apk e importe o JSON. Desinstalar apaga notas e demais preferências salvas no app.

Esta versão tem **Biblioteca** (playlists, álbuns salvos, músicas curtidas e avaliações), **Play na pesquisa** e **avisos com texto branco**. A reprodução Spotify depende de conta Premium e dispositivo ativo.
