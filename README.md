---


---

<h1 id="icqticle">ICQticle</h1>
<p><img src="https://github.com/DippyArtu/ICQticle/blob/master/pics/msg.png" alt="ui"></p>
<h3 id="a-super-primitive-python-messenger-with-chat-bots-support">A super primitive Python messenger with chat-bots support</h3>
<p>This is more of an “ok cool i sort of know how to do this now” exercise, rather than a serious project, still tho.</p>
<p>ICQticle is a fully functional messenger that can be used for things like, sending messages and receiving messages (surprise surprise). This project also has the infrastructure needed to implement a chat-bot of any level of sophistication, although right now, there’s only one which makes awful jokes.</p>
<p>Other than that, there is message pagination, so that the client doesn’t crash, some basic protection (client doesn’t crash when the server is offline) as well as key signal processing (you can send messages with a return button).</p>
<p>I did try to deploy the server on a Heroku platform and a messenger as an app, both successfully, but because I have no plans for actually keeping this thing alive, if you’ll want to try this out, you’ll have to deploy everything locally from your machine, soz.</p>
<h2 id="how-to">How to</h2>
<ul>
<li>
<p>Make sure both you and a person\peeople you will chat with have Python3 installed on their machine as well as all the requirements<br>
<code>-$ pip install flask pyqt5 requests pyjokes</code></p>
</li>
<li>
<p>Go to the project directory and launch the server<br>
<code>-$ python3 server.py</code></p>
</li>
<li>
<p>Make sure you have an <a href="http://ngrok.com">ngrok</a> account and you have connected your account with an auth key</p>
</li>
<li>
<p>Launch ngrok<br>
<code>-$ ./ngrok http 5000</code></p>
</li>
<li>
<p>You should see something like this. Copy the second link in ‘Forwarding’ (the one starting with <code>https://</code> ending with <code>ngrok.io</code>) and paste it into the line 68 in <code>messenger.py</code> file</p>
</li>
</ul>
<p><img src="https://github.com/DippyArtu/ICQticle/blob/master/pics/ngrok.jpg" alt="ngrok"></p>
<ul>
<li>You are good to go! Launch:<br>
<code>-$ python3 messenger.py</code></li>
</ul>
<h1 id="section"></h1>
<p>All messages will be deleted when you restart the server</p>
<p>You don’t have to restart ngrok when you restart the server, but if you do restart ngrok, you’ll have to change the <code>messanger.py</code> to update the adress (all the clients)</p>

