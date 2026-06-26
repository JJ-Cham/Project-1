# 🌱 Sprout

A CLI-based sustainability gamification system where users grow a virtual plant by completing real-world eco-friendly actions. Each action earns XP based on its environmental impact, helping the plant evolve from a tiny seed into a blooming tree 🌳.

Sprout blends environmental data, behavioral tracking, and AI-generated feedback to encourage sustainable habits in a fun, interactive way.

# 🎮 Core Concept

Users interact with Sprout entirely through the command line.

Every eco-friendly action (biking, walking, recycling, public transport) is tracked, converted into carbon savings, and transformed into XP. As XP increases, the plant grows through multiple stages.

# 🌿 Plant Growth Stages

- 🌱 Seed
- 🌱 Sprout
- 🌿 Seedling
- 🌿 Young Plant
- 🌸 Blooming Plant

# 💻 Features

## 🌍 Eco Action Tracking

Users can log sustainable actions such as:

- 🚴 Biking
- 🚶 Walking
- ♻️ Recycling
- 🚌 Public Transport

Each action earns XP based on its environmental impact.

## 🌱 Plant Growth System

- XP accumulates over time
- Plant levels up automatically
- Growth stage updates dynamically
- CLI displays plant progression after every action

## 📊 Data Storage (SQLAlchemy + SQLite)

Sprout uses a SQLite database managed through SQLAlchemy ORM, replacing the previous CSV-based system.

The database stores:

- User profiles
- Plant data
- Action history
- XP progression

This upgrade provides:

- Safer, more reliable data persistence
- Relational structure for cleaner queries
- Easier scaling for future features

## 🌦️ Weather-Based Suggestions (OpenWeather API)

Sprout uses real-time weather data to:

- Suggest eco-friendly actions
- Recommend biking or walking on good weather days
- Suggest indoor eco activities during poor weather

## 🌍 Carbon Impact Tracking (Carbon API)

Using a carbon emissions API (such as Climatiq or Carbon Interface), Sprout:

- Calculates CO₂ savings for each action
- Converts carbon savings into XP
- Provides real-world environmental feedback

## 🧠 AI Feedback System (Google GenAI)

Google GenAI generates:

- 🌱 Personalized plant messages
- 💚 Motivational feedback
- 🎯 Daily eco challenges

### Example

> "Your decision to bike today helped your plant grow stronger roots by reducing carbon emissions!"

# ▶️ How to Run Sprout

## 1. Clone the Repository

```bash
git clone https://github.com/JJ-Cham/Project-1.git
cd Project-1
```

## 2. Create a Virtual Environment

```bash
python3 -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Set Up Environment Variables

Create a `.env` file in the project root:

```env
OPENWEATHER_API_KEY=your_key_here
CARBON_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here
```

> **Note:** You only need the API keys for the services you plan to use.

## 5. Initialize the Database

Sprout will automatically create the SQLite database (`sprout.db`) on first run.

To manually initialize or reset the database:

```bash
python database_setup.py
```

## 6. Run the Game

```bash
python main.py
```

You'll be greeted with:

```text
🌱 Welcome to Sprout!

Username:
Plant name:
```

And your sustainability journey begins!

# 🧾 CLI Gameplay Example

```text
🌱 Welcome to Sprout!

Username: Te
Plant name: st

===== SPROUT =====
1. View Plant
2. Bike
3. Walk
4. Recycle
5. Bus
6. Weather Suggestion
7. View History
8. Exit

> 6
City: Seattle

It's overcast clouds and 13.56° in Seattle — perfect for biking 🚴 or walking 🚶!

===== SPROUT =====
1. View Plant
2. Bike
3. Walk
4. Recycle
5. Bus
6. Weather Suggestion
7. View History
8. Exit

> 3
Distance (km): 15
City: Seattle

--- NEW GROWTH ---
XP: 0 -> 28
Stage: Seedling
```

# 👥 Created By

- **JJ Cham**
- **Sheyla Almanzar-Abreu**
- **Mussie Aregay**

**SEO Tech Developer — Summer Residency**