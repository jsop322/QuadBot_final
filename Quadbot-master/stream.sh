
#! /bin/bash
STREAM_URL="rtmp://live.hitbox.tv/push"
KEY="megatronix?key=X5YWxwUO" # put your key here

 raspivid -n -o - -t 0 -w 800 -h 600 -vf -hf -fps 20 -b 6000000 | ffmpeg  -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i - -vcodec copy -acodec aac -ab 128k -g 50 -strict experimental -f flv "$STREAM_URL/${KEY}"
