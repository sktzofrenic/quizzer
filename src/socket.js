import Pusher from 'pusher-js'

var pusher = new Pusher('c94fbf647eaf623c10ba', {
      cluster: 'us2',
      forceTLS: true
    })

export const socket = pusher.subscribe('ssgame-1');

