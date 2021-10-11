from quart import Quart, render_template, request, session, redirect, url_for
from quart_discord import DiscordOAuth2Session
from discord.ext import ipc

app = Quart(__name__, static_folder="static/")
ipc_client = ipc.Client(secret_key = "Neil")

app.config["SECRET_KEY"] = "test123"
app.config["DISCORD_CLIENT_ID"] = 865886698231824414   # Discord client ID.
app.config["DISCORD_CLIENT_SECRET"] = "2oVU9Q_MtpdZL3bekSsp2D3ngytT6q2C"   # Discord client secret.
app.config["DISCORD_REDIRECT_URI"] = "http://127.0.0.1:5000/callback"   

discord = DiscordOAuth2Session(app)

@app.route("/")
async def home():
	return await render_template("index.html", authorized = await discord.authorized)

@app.route("/login")
async def login():
	return await discord.create_session()

@app.route("/callback")
async def callback():
	try:
		await discord.callback()
	except Exception:
		pass

	return redirect(url_for("dashboard"))

@app.route("/dashboard")
async def dashboard():
	if not await discord.authorized:
		return redirect(url_for("login")) 

	guild_count = await ipc_client.request("get_guild_count")
	guild_ids = await ipc_client.request("get_guild_ids")

	user_guilds = await discord.fetch_guilds()

	guilds = []

	for guild in user_guilds:
		if guild.permissions.administrator:			
			guild.class_color = "green-border" if guild.id in guild_ids else "red-border"
			guilds.append(guild)

	guilds.sort(key = lambda x: x.class_color == "red-border")
	name = (await discord.fetch_user()).name
	return await render_template("dashboard.html", guild_count = guild_count, guilds = guilds, username=name)

@app.route("/dashboard/<int:guild_id>", methods=['POST', 'GET'])
async def dashboard_server(guild_id):
	if not await discord.authorized:
		return redirect(url_for("login")) 

	guild = await ipc_client.request("get_guild", guild_id = guild_id)
	if guild is None:
		return redirect(f'https://discord.com/oauth2/authorize?&client_id={app.config["DISCORD_CLIENT_ID"]}&scope=bot&permissions=8&guild_id={guild_id}&response_type=code&redirect_uri={app.config["DISCORD_REDIRECT_URI"]}')

	channel_name = await ipc_client.request("get_channel_name", guild_id = guild_id)
	channel_id = await ipc_client.request("get_channel_ids", guild_id = guild_id)

	return await render_template("server.html", channel_name = channel_name, channel_id = channel_id)

@app.route('/logout')
async def logout():
	discord.revoke()
	return redirect(url_for("home"))

@app.route("/dashboard/send", methods=['POST'])
async def send():
	if request.method == 'POST':
		data0 = await request.form
		data = data0.to_dict(flat=False)
		print(data)
		channel = data[channel]
		msg = data[msg]
		guild = await ipc_client.request("send_message", channel = channel, msg=msg)
		return "Debug."


if __name__ == "__main__":
	app.run(debug=True)