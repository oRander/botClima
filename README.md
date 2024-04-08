<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>
<body>
    <h1>RandBot</h1>
    <p>O RandBot é um bot Discord que fornece informações meteorológicas e previsão do tempo para uma determinada cidade. Ele é construído usando Python e a biblioteca discord.py.</p>
   <h2>Instalação</h2>
    <p>Para executar o bot, primeiro você precisa instalar todas as dependências. Você pode fazer isso executando o seguinte comando:</p>
    <pre><code>pip install discord.py python-weather pytz</code></pre>
<h2>Como testar</h2>
<ol>
    <li>Adicione o bot <strong>RandBot#9151</strong> ao seu servidor do Discord.</li>
    <li>Use o comando <code>!iniciar</code> para iniciar o bot e receber uma mensagem de boas-vindas.</li>
    <li>Use o comando <code>!clima</code> para obter informações meteorológicas para uma cidade específica.</li>
    <li>Digite a cidade e o estado (formato: cidade, UF) conforme solicitado.</li>
</ol>
<h2>Como usar</h2>
    <ol>
        <li>Crie um bot no <a href="https://discord.com/developers" target="_blank" rel="noopener noreferrer">Discord Developer Portal</a>.</li>
        <li>Copie o token de acesso do bot gerado na página de configurações do bot.</li>
        <li>Abra o arquivo <code>main.py</code> e substitua <code>"SEU_TOKEN_AQUI"</code> pelo token de acesso do seu bot.</li>
        <li>Inicie o bot executando o arquivo <code>main.py</code>.</li>
        <li>O bot ficará online e pronto para aceitar comandos.</li>
        <li>Use os comandos descritos acima para interagir com o bot e obter informações meteorológicas.</li>
    </ol>
 <h2>Contribuição</h2>
    <p>Se você quiser contribuir para o projeto, sinta-se à vontade para fazer um fork e enviar um pull request. Todas as contribuições são bem-vindas!</p>

<h2>Dificuldade</h2>
<p>Encontrei algumas dificuldades ao tentar integrar outras bibliotecas de previsão meteorológica. Inicialmente, tentei utilizar a API do <a href="https://advisor.climatempo.com.br/" target="_blank">Clima Tempo</a>. No entanto, descobri que o acesso às informações estava limitado a um único município, e enfrentei dificuldades para configurar o token relacionado à cidade. Após várias tentativas, decidi trocar para a <a href="https://www.meteomatics.com/" target="_blank">Meteos Matics</a>, que parecia ser a opção mais adequada devido ao plano gratuito oferecido. Infelizmente, ao tentar me cadastrar com dois emails diferentes, recebi a seguinte mensagem de erro:</p>
<blockquote>
<p>Olá RANDER,</p>
<p>Agradecemos o seu interesse pelo nosso API!</p>
<p>Devido a um erro técnico, a sua conta de teste não pôde ser criada.</p>
<p>Por favor, entre em contato conosco através do e-mail sales@meteomatics.com.</p>
<p>Atenciosamente,<br>Equipe de suporte</p>
</blockquote>
<p>Posteriormente, tentei utilizar a <a href="https://openweathermap.org/" target="_blank">Open Weather</a>, porém, descobri que o plano gratuito não seria suficiente para os objetivos do projeto. Por fim, encontrei a biblioteca <a href="https://pypi.org/project/python-weather/" target="_blank">python-weather</a>, que embora apresentasse alguns erros de precisão, era gratuita e atendia às necessidades do projeto.</p>

<p>Quanto à criação do bot, inicialmente optei pelo WhatsApp, utilizando a ferramenta <a href="https://www.twilio.com/pt-br" target="_blank">Twilio</a>. No entanto, descobri que a ferramenta era limitada a um único contato por vez, o que tornava inviável para o propósito desejado.</p>

<p>Depois, foquei na criação de um bot pelo Telegram, pois já havia trabalhado com algo semelhante no passado. No entanto, encontrei dificuldades para buscar a cidade usando os métodos do Telegram, que só lêem a primeira palavra depois da / (barra).</p>

<p>Por fim, consegui criar o bot no Discord, embora não tenha ficado exatamente como eu queria devido às dificuldades encontradas, o que me impediu de concluir tudo o que havia planejado inicialmente.</p>

   
</body>
</html>

