from flask import Blueprint, render_template, request, jsonify
from quizzer.extensions import pusher_client

public_views = Blueprint('game_client', __name__,
                        template_folder='templates/')


@public_views.route('/gm', methods=['GET', 'POST'])
def game_master():
    print(request.method)
    return render_template('/game_master.html')

@public_views.route('/', methods=['GET', 'POST'])
def buzzer():
    print(request.method)
    return render_template('/client.html')

@public_views.route('/api', methods=['GET', 'POST'])
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



