# SoundManager.py
"""Sound manager for Alien Invasion."""

import pygame


class SoundManager:
    """A class to manage all game sounds."""

    def __init__(self):
        """Initialize the sound manager."""
        pygame.mixer.init()
        
        self.volume = 0.5
        self.sounds = {}
        self._load_sounds()

    def _load_sounds(self):
        """Load all sound files."""
        sound_files = {
            'shoot': 'Sounds/shoot.wav',
            'explosion': 'Sounds/explosion.wav',
            'levelup': 'Sounds/levelup.wav',
            'gameover': 'Sounds/gameover.wav'
        }

        for name, filepath in sound_files.items():
            try:
                self.sounds[name] = pygame.mixer.Sound(filepath)
                self.sounds[name].set_volume(self.volume)
            except pygame.error:
                print(f"Warning: Could not load {filepath}")
                self.sounds[name] = None

    def play(self, sound_name):
        """Play a sound by name."""
        if sound_name in self.sounds and self.sounds[sound_name]:
            self.sounds[sound_name].play()

    def set_volume(self, volume):
        """Set volume for all sounds (0.0 to 1.0)."""
        self.volume = max(0.0, min(1.0, volume))
        for sound in self.sounds.values():
            if sound:
                sound.set_volume(self.volume)

    def mute(self):
        """Mute all sounds."""
        self.set_volume(0.0)

    def unmute(self):
        """Unmute sounds."""
        self.set_volume(0.5)