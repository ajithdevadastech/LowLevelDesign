class AudioPlayer(object):
    def play_audio(self):
        raise NotImplementedError
    def stop_audio(self):
        raise NotImplementedError
    def adjust_audio_volume(self):
        raise NotImplementedError

class VideoPlayer(object):
    def play_video(self):
        raise NotImplementedError
    def stop_video(self):
        raise NotImplementedError
    def adjust_video_brightness(self):
        raise NotImplementedError

class MP3Player(AudioPlayer):
    def play_audio(self):
        #add logic
    def stop_audio(self):
        #add logic
    def adjust_audio_volume(self):
        #add logic

class AviVideoPlayer(VideoPlayer):
    def play_video(self):
        #add logic
    def stop_video(self):
        #add logic
    def adjust_video_brightness(self):
        #add logic

"""
the Media player class is split and the methods are used only in relevant cases
"""

class MultiMediaPlayer(AudioPlayer, VideoPlayer):
    def play_audio(self):
        #add logic
    def play_video(self):
        #add logic

    def stop_audio(self):
        #add logic
    def stop_video(self):
        #add logic
    def adjust_audio_volume(self):
        #add logic
    def adjust_video_brightness(self):
        #add logic

