class MediaPlayer(object):
    def play_audio(self):
        raise NotImplementedError
    def play_video(self):
        raise NotImplementedError
    def stop_audio(self):
        raise NotImplementedError
    def stop_video(self):
        raise NotImplementedError
    def adjust_audio_volume(self):
        raise NotImplementedError
    def adjust_video_brightness(self):
        raise NotImplementedError

    """
    This abides to single responsibilty as Mediaplayer has these responsibilities.
    But the interface would be forced to implement all the methods, even if it doesn't need them.
    so its better the split the responsbilities into audioplayer and video player
    """
