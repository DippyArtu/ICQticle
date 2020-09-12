import time
import pyjokes

help_ = "This is the helpful the /help command\n available commands: \n /joke — it's not worth it"

# info_ = "Your name is {name}\n There are {cntUsers} users in chat\n To see chat users type /users".format(name = data['name'], cntUsers = statusInfo['users_count'])


def bot(bot_command, database):
    if bot_command == '/help':
        message = help_
    elif bot_command == '/joke':
        message = str(pyjokes.get_joke(language='en', category='all'))
    # elif bot_command == '/info':
    #     message = info_
    else:
        message = bot_command

    database.append({
        'id': len(database),
        'name': '_BOT_',
        'text': message,
        'timestamp': time.time()
    })
    return{'ok': True}
