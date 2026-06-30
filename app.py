import streamlit as st


st.set_page_config(
    page_title="PitchWise AI",
    page_icon="PW",
    layout="wide",
)


TEAM_PROFILES = {
    "Argentina": {
        "attack": 87,
        "defense": 82,
        "midfield": 85,
        "recent_form": 88,
        "pressure": 91,
        "style": "patient buildup, compact defending, and high emotional control",
    },
    "Brazil": {
        "attack": 90,
        "defense": 80,
        "midfield": 84,
        "recent_form": 83,
        "pressure": 86,
        "style": "wide attacking play, technical overloads, and fast transitions",
    },
    "France": {
        "attack": 89,
        "defense": 84,
        "midfield": 83,
        "recent_form": 86,
        "pressure": 88,
        "style": "direct attacking speed, strong defensive recovery, and set-piece threat",
    },
    "England": {
        "attack": 84,
        "defense": 85,
        "midfield": 86,
        "recent_form": 82,
        "pressure": 78,
        "style": "structured possession, crossing options, and controlled defensive shape",
    },
    "Spain": {
        "attack": 82,
        "defense": 83,
        "midfield": 90,
        "recent_form": 84,
        "pressure": 82,
        "style": "possession control, short passing, and midfield pressing traps",
    },
    "Germany": {
        "attack": 83,
        "defense": 78,
        "midfield": 84,
        "recent_form": 79,
        "pressure": 84,
        "style": "vertical passing, late box arrivals, and aggressive counter-pressing",
    },
    "Portugal": {
        "attack": 86,
        "defense": 81,
        "midfield": 85,
        "recent_form": 85,
        "pressure": 83,
        "style": "creative midfield play, flexible forwards, and patient final-third attacks",
    },
    "Netherlands": {
        "attack": 81,
        "defense": 86,
        "midfield": 82,
        "recent_form": 81,
        "pressure": 80,
        "style": "wing-back width, aerial strength, and disciplined defensive blocks",
    },
    "United States": {
        "attack": 76,
        "defense": 77,
        "midfield": 79,
        "recent_form": 78,
        "pressure": 74,
        "style": "athletic pressing, quick counters, and energetic midfield duels",
    },
    "Japan": {
        "attack": 78,
        "defense": 80,
        "midfield": 81,
        "recent_form": 82,
        "pressure": 79,
        "style": "coordinated pressing, quick passing, and disciplined team movement",
    },
}


EVENT_EXPLANATIONS = {
    "Early goal": {
        "momentum": "The scoring team can defend with more patience, while the opponent may attack earlier than planned.",
        "trust": "A model should not treat the goal as the whole story; shot quality, time remaining, and tactical response still matter.",
    },
    "Red card": {
        "momentum": "The team with fewer players usually loses pressing power and must protect central spaces more carefully.",
        "trust": "Fans often see this as decisive, but timing and scoreline decide whether the impact is extreme or manageable.",
    },
    "Penalty decision": {
        "momentum": "A penalty can change both the score and the emotional temperature of the match.",
        "trust": "A transparent explanation should separate the rule question from the emotional reaction around the decision.",
    },
    "Substitution": {
        "momentum": "Fresh legs can change pressing intensity, attacking width, or defensive stability.",
        "trust": "The effect depends on role fit, not only player reputation.",
    },
    "Defensive shape change": {
        "momentum": "Dropping deeper can reduce space behind the defense but may invite pressure and second balls.",
        "trust": "This can look passive to fans, even when it is a deliberate risk-control choice.",
    },
    "VAR review": {
        "momentum": "Long reviews interrupt rhythm and can raise anxiety for players and supporters.",
        "trust": "Fans trust the result more when the decision is explained in simple rule-based language.",
    },
}


def explain_feature(label, value_a, value_b, team_a, team_b):
    gap = value_a - value_b
    if abs(gap) < 4:
        return f"{label} is almost even, so it does not strongly separate {team_a} and {team_b}."
    leader = team_a if gap > 0 else team_b
    trailer = team_b if gap > 0 else team_a
    return f"{leader} has the clearer {label.lower()} edge over {trailer}, which pushes the match narrative toward {leader}."


def score_team(profile, venue_boost, pressure_multiplier):
    base = (
        profile["attack"] * 0.28
        + profile["defense"] * 0.22
        + profile["midfield"] * 0.22
        + profile["recent_form"] * 0.18
        + profile["pressure"] * 0.10
    )
    return base + venue_boost + (profile["pressure"] - 80) * pressure_multiplier


def probability_view(score_a, score_b):
    total = score_a + score_b
    draw = max(14, 28 - abs(score_a - score_b) * 1.4)
    remaining = 100 - draw
    share_a = score_a / total
    win_a = remaining * share_a
    win_b = remaining - win_a
    return round(win_a, 1), round(draw, 1), round(win_b, 1)


def fan_explanation(level, team_a, team_b, profile_a, profile_b, event):
    if level == "Beginner":
        return (
            f"Think of this as a story about control. {team_a} plays with {profile_a['style']}, while "
            f"{team_b} relies on {profile_b['style']}. The selected event, {event.lower()}, can change "
            "who feels calm, who takes risks, and which spaces become important."
        )
    if level == "Casual fan":
        return (
            f"The matchup depends on which team can make the game feel like its preferred style. "
            f"{team_a} wants {profile_a['style']}; {team_b} wants {profile_b['style']}. "
            f"A {event.lower()} matters because it can change tempo, confidence, and the tactical risks each side accepts."
        )
    return (
        f"Analyst view: compare phase control and risk transfer. {team_a}'s profile emphasizes {profile_a['style']}; "
        f"{team_b}'s profile emphasizes {profile_b['style']}. The {event.lower()} scenario should be judged by its effect "
        "on compactness, pressing access, chance quality, and emotional decision-making under pressure."
    )


st.title("PitchWise AI")
st.caption("An explainable World Cup companion that helps fans understand the match story, not just the result.")

with st.sidebar:
    st.header("Match Setup")
    teams = list(TEAM_PROFILES.keys())
    team_a = st.selectbox("Team A", teams, index=0)
    team_b = st.selectbox("Team B", teams, index=1)
    fan_level = st.selectbox("Fan knowledge level", ["Beginner", "Casual fan", "Analyst"])
    venue = st.selectbox("Venue context", ["Neutral World Cup venue", "Team A home-like crowd", "Team B home-like crowd"])
    pressure_level = st.slider("Pressure level", 1, 10, 7)
    event = st.selectbox("Match event to explain", list(EVENT_EXPLANATIONS.keys()))

if team_a == team_b:
    st.warning("Choose two different teams to compare the match story.")
    st.stop()

profile_a = TEAM_PROFILES[team_a]
profile_b = TEAM_PROFILES[team_b]

venue_boost_a = 0
venue_boost_b = 0
if venue == "Team A home-like crowd":
    venue_boost_a = 2.5
elif venue == "Team B home-like crowd":
    venue_boost_b = 2.5

pressure_multiplier = (pressure_level - 5) / 20
score_a = score_team(profile_a, venue_boost_a, pressure_multiplier)
score_b = score_team(profile_b, venue_boost_b, pressure_multiplier)
p_a, p_draw, p_b = probability_view(score_a, score_b)

left, middle, right = st.columns(3)
left.metric(f"{team_a} outlook", f"{p_a}%")
middle.metric("Draw tension", f"{p_draw}%")
right.metric(f"{team_b} outlook", f"{p_b}%")

st.progress(p_a / 100, text=f"{team_a} match outlook")
st.progress(p_draw / 100, text="Draw / unresolved tension")
st.progress(p_b / 100, text=f"{team_b} match outlook")

st.subheader("Why The AI Leans This Way")
reasons = [
    explain_feature("Attack", profile_a["attack"], profile_b["attack"], team_a, team_b),
    explain_feature("Defense", profile_a["defense"], profile_b["defense"], team_a, team_b),
    explain_feature("Midfield control", profile_a["midfield"], profile_b["midfield"], team_a, team_b),
    explain_feature("Recent form", profile_a["recent_form"], profile_b["recent_form"], team_a, team_b),
    explain_feature("Pressure handling", profile_a["pressure"], profile_b["pressure"], team_a, team_b),
]

for reason in reasons:
    st.write(f"- {reason}")

st.subheader("Fan-Friendly Match Explanation")
st.write(fan_explanation(fan_level, team_a, team_b, profile_a, profile_b, event))

event_info = EVENT_EXPLANATIONS[event]
event_col, trust_col = st.columns(2)
with event_col:
    st.subheader("Momentum Lens")
    st.write(event_info["momentum"])
with trust_col:
    st.subheader("Trust & Transparency Lens")
    st.write(event_info["trust"])

st.subheader("Human-Centered Takeaway")
leader = team_a if p_a > p_b else team_b
st.write(
    f"PitchWise AI does not replace coaches, referees, or analysts. It helps fans ask better questions: "
    f"why {leader} may have the current edge, what could shift momentum, and which parts of the match are tactical, "
    "emotional, or rule-driven."
)

st.caption(
    "Prototype note: this hackathon version uses an explainable scoring model and AI-generated narrative logic. "
    "IBM Bob was used as the IBM AI-supported development tool for building and refining the prototype."
)
