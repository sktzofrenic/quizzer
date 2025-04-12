import Pusher from 'pusher-js'

var pusher = new Pusher('586ed4c0c7863354b01f', {
      cluster: 'us2',
      forceTLS: true
    })

export const socket = pusher.subscribe('ssgame-1');

