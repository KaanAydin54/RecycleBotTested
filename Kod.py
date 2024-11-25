import discord
intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Merhaba {client.user}! benim çevre dostu botuma hoşgeldin')
    if message.content.startswith("Çevre kirliliği nedir"):
        await message.channel.send('Çevrenin canlı ve cansız öğelerini olumsuz yönde etkileyen, üzerinde yapısal zararlar meydana getiren ve niteliklerini bozan yabancı maddelerin hava, su ve toprağa yoğun bir şekilde karışması olayına “çevre kirliliği” adı verilmektedir. Çevrenin doğal olmayan bir şekilde insan eliyle bozulmasıdır.')
    if message.content.startswith('Su kirliliği nedir'):
        with open("sukirliligi.jpg", "rb") as f:
            resim = discord.File(f)
        await message.channel.send(file = resim)
        await message.channel.send('Okyanus, göl ve nehir gibi su kaynaklarının plastik atıklar, kimyasal atıklar ve mikroorganizmalar gibi zararlı maddelerden kirlenmesine ve suyun çevreye ve insan sağlığına zararlı hale gelmesine su kirliliği denir. Su kirliliği, yaşamın her alanını olumsuz etkilediğinden dolayı canlı yaşamı için büyük risktir.')
    if message.content.startswith('Toprak kirliliği nedir'):
        with open("toprakkirliaga.jpg", "rb") as f:
            resim = discord.File(f)
        await message.channel.send(file = resim)
        await message.channel.send(' (plastik vb gibi toprakta çözünmeyen maddeler), sıvı (atık yağ gibi çevreyi kirletici maddeler), radyoaktif atık ve diğer kirletici unsurlar tarafından toprağın fiziksel ve kimyasal özelliklerinin bozulmasına toprak kirliliği denilmektedir.')
    if message.content.startswith('Hava kirliliği nedir'):
        with open("havakirliligi.jpg", "rb") as f:
            resim = discord.File(f)
        await message.channel.send(file = resim)
        await message.channel.send('Hava kirliliği, havanın doğal bileşiminin çeşitli nedenlerle değişmesi, havada katı, sıvı ve gaz şeklindeki yabancı maddelerin insan sağlığına, canlı hayatına, ekolojik dengeye ve eşyalara zararlı olabilecek derişim ve sürede bulunmasıdır.')
    if message.content.startswith('Çevre kirliliğini önlemek için neler yapmalıyız'):
        await message.channel.send('Kirliliğe engel olun. Yerlere çöp atmayın, geri dönüşüme katkı sağlayın. Dişinizi fırçalarken, banyo yaparken ve mutfakta çeşmeyi açık bırakmayın.Kişisel matara kullanarak, pet şişe kullanımını azaltın.')



client.run(" TOKEN HERE")
