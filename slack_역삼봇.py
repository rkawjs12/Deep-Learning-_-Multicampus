{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "RuntimeError",
     "evalue": "This event loop is already running",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mRuntimeError\u001b[0m                              Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-a7c71e3724e2>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     24\u001b[0m \u001b[0mslack_token\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'xoxb-726528928834-737979588784-mLnN0NPfHx7NVnkBYYsayJxC'\u001b[0m  \u001b[1;31m# Bot User OAuth Access Token\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     25\u001b[0m \u001b[0mrtm_client\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mslack\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mRTMClient\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtoken\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mslack_token\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 26\u001b[1;33m \u001b[0mrtm_client\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mstart\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\slack\\rtm\\client.py\u001b[0m in \u001b[0;36mstart\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    195\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mfuture\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    196\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 197\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_event_loop\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrun_until_complete\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfuture\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    198\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    199\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mstop\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\asyncio\\base_events.py\u001b[0m in \u001b[0;36mrun_until_complete\u001b[1;34m(self, future)\u001b[0m\n\u001b[0;32m    569\u001b[0m         \u001b[0mfuture\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0madd_done_callback\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0m_run_until_complete_cb\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    570\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 571\u001b[1;33m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrun_forever\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    572\u001b[0m         \u001b[1;32mexcept\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    573\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mnew_task\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0mfuture\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdone\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mand\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mfuture\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcancelled\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\asyncio\\base_events.py\u001b[0m in \u001b[0;36mrun_forever\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    524\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_check_closed\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    525\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mis_running\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 526\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mRuntimeError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'This event loop is already running'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    527\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mevents\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_get_running_loop\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    528\u001b[0m             raise RuntimeError(\n",
      "\u001b[1;31mRuntimeError\u001b[0m: This event loop is already running"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import slack\n",
    "\n",
    "@slack.RTMClient.run_on(event='message')\n",
    "def say_hello(**payload):\n",
    "    data = payload['data']\n",
    "    print(data)\n",
    "    print('=====\\n')\n",
    "\n",
    "    web_client = payload['web_client']\n",
    "    rtm_client = payload['rtm_client']\n",
    "    if 'text' in data.keys() and 'Hello' in data['text']:\n",
    "        channel_id = data['channel']\n",
    "        thread_ts = data['ts']\n",
    "        user = data['user']\n",
    "\n",
    "        web_client.chat_postMessage(\n",
    "            channel='#general',\n",
    "            text=f\"Hi <@{user}>!\", # 상대방 이름을 넣어 대답한다\n",
    "            #thread_ts=thread_ts\n",
    "        )\n",
    "\n",
    "#slack_token = os.environ[\"SLACK_API_TOKEN\"]\n",
    "slack_token = 'xoxb-726528928834-737979588784-mLnN0NPfHx7NVnkBYYsayJxC'  # Bot User OAuth Access Token\n",
    "rtm_client = slack.RTMClient(token=slack_token)\n",
    "rtm_client.start()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
