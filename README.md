# Project-1
# 🌱 Sprout

Sprout is a CLI-based sustainability gamification system where users grow a virtual plant by completing real-world eco-friendly actions. Each action earns XP based on environmental impact, which helps the plant evolve through different growth stages—from a seed to a fully grown tree 🌳.

The project combines real environmental data, behavioral tracking, and AI-generated feedback to encourage sustainable habits in an engaging and interactive way.

---

# 🎮 Core Concept

Users interact with Sprout entirely through the command line.

Every eco-friendly action (bike, walk, recycle, public transport) is tracked, converted into carbon savings, and transformed into XP. As XP increases, the plant grows and evolves through stages.

## 🌿 Plant Growth Stages
- Seed 🌱  
- Sprout 🌱  
- Seedling 🌿  
- Young Plant 🌿  
- Blooming Plant 🌸  
- Tree 🌳  

---

# 💻 Features

## 🌍 Eco Action Tracking
Users can log sustainable actions such as:
- biking 🚴
- walking 🚶
- recycling ♻️
- public transport 🚌

Each action earns XP based on environmental impact.

---

## 🌱 Plant Growth System
- XP accumulates over time
- Plant levels up automatically
- Growth stage updates dynamically
- CLI displays plant progression after every action

---

## 📊 Data Storage (SQL Database)
Sprout uses CSV files powered by Pandas to store:

- Users
- Plant profiles
- Action history
- XP progression


---

## 🌦️ Weather-Based Suggestions (OpenWeather API)
The system uses weather data to:
- suggest eco-friendly actions
- recommend biking/walking on good weather days
- suggest indoor eco activities on bad weather days

---

## 🌍 Carbon Impact Tracking (Carbon API)
Uses a carbon emissions API (e.g., Climatiq / Carbon Interface) to:
- calculate CO₂ savings per action
- convert actions into XP values
- provide real-world environmental feedback

---

## 🧠 AI Feedback System (Google GenAI)
Google GenAI generates:
- personalized plant messages 🌱
- motivational feedback
- daily eco challenges

Example:
> Your decision to bike today helped your plant grow stronger roots by reducing carbon emissions!

---

# 🧾 CLI Commands

## 🌱 Create Plant
```bash
create_plant Sprout

```
## Created by JJ Cham, Sheyla Almanzar-Abreu, & Mussie Aregay
### SEO Tech Developer