import requests
from flask import (
    Blueprint,
    jsonify,
    redirect,
    render_template,
    request,
    send_from_directory,
)

from quizzer.extensions import pusher_client
from quizzer.settings import Config

public_views = Blueprint('game_client', __name__,
                        template_folder='templates/')


@public_views.route('/gm', methods=['GET', 'POST'])
def game_master():
    print(request.method)
    return render_template('/game_master.html')

@public_views.route('/files', methods=['GET', 'POST'])
def files():
    print(request.method)
    return render_template('/files.html')

@public_views.route('/pope', methods=['GET', 'POST'])
def pope_micah():
    print(request.method)
    return render_template('/pope.html')

@public_views.route('/noooo', methods=['GET', 'POST'])
def noooo():
    print(request.method)
    
    # Transaction email HTML template
    transaction_email_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f4; }
            .container { max-width: 600px; margin: 20px auto; background-color: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            .header { background-color: #4CAF50; color: white; padding: 20px; text-align: center; }
            .content { padding: 30px; }
            .transaction-details { background-color: #f9f9f9; padding: 20px; border-radius: 5px; margin: 20px 0; }
            .detail-row { display: flex; justify-content: space-between; margin: 10px 0; padding-bottom: 10px; border-bottom: 1px solid #e0e0e0; }
            .detail-row:last-child { border-bottom: none; }
            .label { color: #666; font-weight: 600; }
            .value { color: #333; font-weight: bold; }
            .amount { font-size: 24px; color: #4CAF50; font-weight: bold; text-align: center; margin: 20px 0; }
            .footer { background-color: #f8f8f8; padding: 20px; text-align: center; color: #666; font-size: 12px; }
            .button { display: inline-block; padding: 12px 30px; background-color: #4CAF50; color: white; text-decoration: none; border-radius: 5px; margin: 20px 0; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Click'd!!!!</h1>
            </div>
            <div class="content">
                <p>There was definitely a click</p>
            </div>
            <div class="footer">
                <p>This is an automated message. Please do not reply to this email.</p>
                <p>&copy; 2025 DANWINS LLC. All rights reserved.</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    # Prepare email data
    data = {
        'from': 'noreply@drxapp.com',
        'to': 'dan@danwins.com',  # Replace with actual recipient
        'subject': 'IT WAS CLICKED!!',
        'html': transaction_email_html 
    }

    print(Config.MAILGUN_API_KEY, 'the key')
    
    result = requests.post(
        "https://api.mailgun.net/v3/drxapp.com/messages",
        auth=("api", Config.MAILGUN_API_KEY),
        data=data,
        verify=False
    )

    print(result)

    return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

@public_views.route('/feud', methods=['GET', 'POST'])
def family_feud():
    print(request.method)
    return send_from_directory('templates', 'family_feud.html')

@public_views.route('/', methods=['GET', 'POST'])
def buzzer():
    print(request.method)
    return render_template('/client.html')

@public_views.route('/sts', methods=['GET', 'POST'])
def sts():
    print(request.method)
    return redirect('https://drx-danwins.us-east-1.linodeobjects.com/danwinsrx1/new_file05242025_31_18Searching%20the%20Scriptures%20-%20Handout.pdf')

@public_views.route('/client/api', methods=['GET', 'POST'])
def verse_api():

    if request.args.get('getCurrentQuestion'):
        pusher_client.trigger('ssgame-1', 'updateClients', {})
        print('updating clients')
        return jsonify({
            'status': 'success'
        })
    if request.args.get('newQuestion', None):
        pusher_client.trigger('ssgame-1', 'newQuestion', {
            'question': request.args.get('question'),
            'choices': request.args.get('choices')
        })
        return jsonify({
            'status': 'success'
        })
    if request.args.get('answer', None):
        pusher_client.trigger('ssgame-1', 'answer', {
            'name': request.args.get('name'), 
            'timestamp': request.args.get('timestamp', None), 
            'question': request.args.get('question'), 
            'letterResponse': request.args.get('letterResponse'),
            'points': request.args.get('points')}
        )
        return jsonify({
            'status': 'success'
        })
    return jsonify({
        'status': 'failure'
    })



