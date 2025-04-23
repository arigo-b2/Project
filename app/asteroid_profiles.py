def get_asteroid_data() -> list:
    asteroid_data = [
        {
            "name": "Apophis",
            "slug": "99942_apophis",
            "desc": """
    Asteroid 99942 Apophis is a near-Earth object that will make an extraordinarily close pass by our planet on April 13, 2029 — coming within just 32,000 kilometers of Earth's surface, closer than many satellites in geosynchronous orbit. Measuring approximately 340 to 450 meters in length, Apophis is roughly the size of a skyscraper and is classified as an S-type (stony) asteroid. Discovered in 2004, Apophis initially caused concern due to early projections that showed a potential Earth impact in 2029 or later. However, after nearly two decades of tracking and orbital refinement, scientists have confidently ruled out any collision risk for at least the next 100 years (NASA, 2024).
    <br><br>
    Despite the lack of threat, the 2029 flyby presents a once-in-a-lifetime scientific opportunity. It is the closest predicted approach of an asteroid this large in recorded human history, and it will occur while Earth has the technological capability to observe it in real time. As Apophis passes by, Earth’s gravity will exert measurable forces on it — stretching, squeezing, and twisting the asteroid in a process that may alter its spin rate and orientation. In some regions with steep slopes, gravitational tidal forces may even trigger minor landslides or surface disturbances on the asteroid. These physical responses offer scientists a unique opportunity to learn about Apophis’s internal structure, material strength, and surface composition by observing how it reacts to Earth’s pull. NASA’s OSIRIS-REx spacecraft, now renamed OSIRIS-APEX, is en route to rendezvous with Apophis after its successful sample return from asteroid Bennu (NASA, 2024).
    <br><br>
    Read More: <a href="https://science.nasa.gov/solar-system/asteroids/apophis-facts/">https://science.nasa.gov/solar-system/asteroids/apophis-facts/</a>
            """
        },
     {
            "name": "Bennu",
            "slug": "101955_bennu",
            "desc": """
    Bennu is a carbonaceous near-Earth asteroid about 490 meters in diameter and rich in primitive organic material. It orbits the Sun every 1.2 years and has a very Earth-like orbit, placing it in the Apollo group of asteroids.  
    Bennu is classified as a potentially hazardous asteroid (PHA) due to its high impact probability (1 in 1750 by 2300) and close Earth flybys, particularly in the late 2100s.  
    What makes Bennu remarkable is its role in planetary science—NASA’s OSIRIS-REx mission successfully collected samples from its surface in 2020, returning them to Earth in 2023. These samples are helping scientists understand the early solar system.  
    Bennu rotates once every 4.3 hours and has a "rubble pile" structure with loosely bound rocks and low density. A potential impact with Bennu would release energy equivalent to 1,200 megatons of TNT.
    <br><br>
    Read More: <a href="https://science.nasa.gov/solar-system/asteroids/101955-bennu/facts/">https://science.nasa.gov/solar-system/asteroids/101955-bennu/facts/</a>
    """
        },   
        {
            "name": "Florence",
            "slug": "3122_florence",
            "desc": """
    Florence is one of the largest known near-Earth asteroids, measuring a massive 4.4 kilometers in diameter. It passed safely by Earth in 2017 at a distance of 7 million km but remains a significant object due to its sheer size and mass.  
    Florence is particularly interesting because it has two small moons, making it one of the few triple asteroid systems ever observed in the near-Earth population. Its rotation period is about 2.4 hours, and its surface composition suggests a stony S-type asteroid.  
    While Florence currently poses no impact threat, its size gives it the potential to cause global-scale devastation in the extremely unlikely case of an Earth impact. Studies of Florence help refine radar imaging and orbital mechanics models for large NEOs.
    """
        },
        {
            "name": "2023 DW",
            "slug": "2023_dw",
            "desc": """
    Asteroid 2023 DW is a small near-Earth object (NEO), approximately 49 meters in diameter, currently being closely monitored by NASA for its predicted close approach to Earth on February 14, 2046. Current projections show that the asteroid will pass safely at a distance of around 4.7 million kilometers — more than 12 times the distance to the Moon. While the probability of impact for this asteroid is just 0.18%, the asteroid has still drawn attention due to its relatively close flyby and the energy it could unleash if it were to enter Earth’s atmosphere (Bonderud, 2023).
    <br><br>
    This flyby, though low-risk, is part of the broader challenge of understanding and monitoring NEOs. An asteroid of this size would likely burn up in the atmosphere, but could still cause regional damage if fragments reached the surface. The asteroid’s highly eccentric orbit means it experiences varying gravitational forces as it travels through the inner solar system, especially near its closest points to the Sun and planets, which could slightly modify its future path.
    <br><br>
    Read More: <a href="https://now.northropgrumman.com/asteroid-2023-dw-everything-you-need-to-know-about-the-next-close-call/">https://now.northropgrumman.com/asteroid-2023-dw-everything-you-need-to-know-about-the-next-close-call/</a>
    """
        },
        {
            "name": "Didymos",
            "slug": "65803_didymos",
            "desc": """
    Didymos is a binary asteroid system consisting of a primary asteroid (~780 meters) and a moonlet called Dimorphos (~160 meters). It orbits the Sun every 2.1 years and is a member of the Apollo group of near-Earth asteroids.  
    Didymos gained global attention as the target of NASA’s DART mission (2022)—the first real-world test of asteroid deflection. DART successfully impacted Dimorphos, shortening its orbital period by 33 minutes, proving that kinetic impactors can alter asteroid trajectories.  
    The Didymos system is a crucial proof-of-concept for planetary defense technologies. Its binary nature also provides rare insight into tidal forces, mutual orbital evolution, and surface cohesion in small bodies.  
    While Didymos itself is not a threat, its configuration and accessibility make it one of the most important objects for long-term planetary risk reduction studies.
    """
        },
        {
            "name": "Toutatis",
            "slug": "4179_toutatis",
            "desc": """
    Toutatis is a highly elongated asteroid (~4.5 km long) with a tumbling, chaotic rotation that makes it one of the most unique objects observed. It passed Earth at a safe distance multiple times and was extensively imaged by radar and the Chang’e 2 mission. Its irregular motion provides valuable data on gravitational torques and non-uniform mass distribution in NEOs. While not a current threat, its size and proximity warrant occasional monitoring, especially due to its near-resonant orbital characteristics with Earth.
    """
        },
        {
            "name": "Ryugu",
            "slug": "162173_ryugu",
            "desc": """
    Ryugu is a C-type asteroid with a diameter of ~900 meters. Its surface was sampled by the Japanese Hayabusa2 mission, which returned material to Earth in 2020. Ryugu’s structure is porous, with evidence of hydrated minerals suggesting early solar system water content. Though not a threat, Ryugu is critical for understanding asteroid cohesion and formation. It provides benchmarks for how weakly bound rubble piles behave under solar radiation and spin-up forces that might eventually lead to fragmentation.
    """
        },
        {
            "name": "Ganymed",
            "slug": "1036_ganymed",
            "desc": """
    Ganymed is the largest known near-Earth asteroid at over 35 km in diameter. Although its orbit keeps it safely distant from Earth, its mass and volume make it a keystone object for planetary science and impact modeling. Ganymed is also of interest due to its spectral similarities with inner belt asteroids, suggesting cross-region migration in the early solar system. Its observations contribute to long-term risk assessments of exceptionally massive NEOs.
    """
        },
        {
            "name": "Phaethon",
            "slug": "3200_phaethon",
            "desc": """
    Phaethon is an unusual near-Earth object in that it behaves like a hybrid asteroid-comet. It is the parent body of the Geminid meteor shower, and its extremely close perihelion (~0.14 AU) causes it to shed dust like a comet. At 5.1 km in diameter, Phaethon is unusually large for a meteor-shower progenitor. Its blue color and high thermal stress cycling make it a fascinating subject for surface evolution studies. While not immediately hazardous, its orbital characteristics put it under regular review by planetary defense programs.
    """
        },
        {
            "name": "1998 OR2",
            "slug": "52768_1998_or2",
            "desc": """
    1998 OR2 is a stony asteroid approximately 2.1 kilometers in diameter that made a close approach in April 2020 at ~6.3 million km. It is one of the largest potentially hazardous asteroids (PHAs) due to its size and Earth-crossing orbit. Its reflective surface and stable rotation make it ideal for radar observations and shape modeling. While currently not on a collision course, its orbital uncertainty remains under refinement, especially beyond the 2100s. It serves as a training ground for impact mitigation strategies and ground-based telescopic coordination.
    """
        },
    ]

    return asteroid_data