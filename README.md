# 👾 Alien Invasion

A classic arcade-style space shooter game built with Python and Pygame.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎮 Gameplay

Defend Earth from waves of alien invaders! Control your spaceship, shoot down aliens, and survive as long as possible. Each wave gets progressively harder.

## ✨ Features

- 🚀 Smooth player-controlled spaceship
- 👾 Dynamic alien fleet with movement patterns
- 🔫 Bullet firing system (max 3 bullets)
- 📊 Score and high score tracking
- ❤️ Lives system (3 ships)
- 📈 Progressive difficulty (speed increases each level)
- 🎯 Level progression
- ⏸️ Pause functionality
- 🖱️ Start menu with Play button

## 🕹️ Controls

| Key | Action |
|-----|--------|
| ← → | Move ship left/right |
| Space | Fire bullet |
| P | Pause/Resume |
| Q / ESC | Quit game |
| Mouse Click | Start game |

## 📁 Project Structure

```
AlienInvasion/
├── AlienInvasion.py
├── Ship.py
├── Alien.py
├── Bullet.py
├── Settings.py
├── GameStats.py
├── Scoreboard.py
├── Button.py
├── high_score.txt
└── Images/
    ├── Ship.bmp
    └── Alien.bmp
```

## 🚀 Installation

1. Clone the repository
```bash
git clone https://github.com/VanitasCodes/AlienInvasion.git
cd AlienInvasion
```

2. Install dependencies
```bash
pip install pygame
```

3. Run the game
```bash
python AlienInvasion.py
```

## 📋 Requirements

- Python 3.x
- Pygame 2.x

## 🎯 How to Play

1. Click Play to start
2. Use arrow keys to move your ship
3. Press Space to shoot bullets
4. Destroy all aliens to advance to the next level
5. Avoid letting aliens hit your ship or reach the bottom
6. You have 3 lives - game ends when all are lost
7. Try to beat your high score!

## 🔧 Game Settings

| Setting | Value |
|---------|-------|
| Starting Lives | 3 |
| Max Bullets | 3 |
| Alien Points | 50 (increases per level) |
| Speed Increase | 10% per level |

## 🚧 Future Enhancements

- [ ] Sound effects
- [ ] Explosion animations
- [ ] Power-ups
- [ ] Multiple alien types
- [ ] Boss battles

## 📄 License

This project is open source and available under the MIT License.

---