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
    Asteroid 101955 Bennu is a small, carbon-rich near-Earth object roughly 500 meters wide at its equator — just about the height of the Empire State Building. Discovered in 1999, Bennu was selected as the target of NASA’s OSIRIS-REx mission, which successfully collected a sample from the asteroid’s surface and returned it to Earth in 2023. Though it poses no immediate danger, Bennu's composition and dynamic orbit make it a crucial object for studying the early solar system and evaluating asteroid impact risks (NASA, 2024).
    <br><br>
    Bennu is believed to have broken off from a much larger carbonaceous asteroid between 700 million and 2 billion years ago, most likely in the main asteroid belt between Mars and Jupiter. Its journey to a near-Earth orbit was guided by gravitational interactions with the giant planets and the Yarkovsky effect — a small but persistent force caused by the re-emission of solar heat. When NASA’s OSIRIS-REx spacecraft collected its sample, scientists were surprised to find the asteroid's surface so loosely packed that the spacecraft would have sunk into it had it not fired its thrusters to retreat. This revealed that Bennu’s surface behaves more like a loosely bound rubble pile than a solid rock.
    <br><br>
    Read More: <a href="https://science.nasa.gov/solar-system/asteroids/101955-bennu/facts/">https://science.nasa.gov/solar-system/asteroids/101955-bennu/facts/</a>
    """
        },   
        {
            "name": "Didymos",
            "slug": "65803_didymos",
            "desc": """
    Asteroid 65803 Didymos is a near-Earth object belonging to the Apollo group, known for its Earth-crossing orbit and binary configuration. The primary body, roughly 780 meters in diameter, is orbited by a smaller moonlet named Dimorphos, measuring about 160 meters. Though not considered a threat, the Didymos system passes close to Earth on a regular basis — within 0.05 AU during some encounters. These orbital characteristics place Didymos in a key category of objects for planetary risk modeling: moderately sized, dynamically active, and periodically proximal to Earth. As such, Didymos is a high-priority target for long-term observation and contingency planning within the context of asteroid impact hazard assessment (NASA, 2024).
    <br><br>
    Didymos is particularly interesting from a risk analysis standpoint due to its rapid rotation, elongated orbit, and binary structure. The primary asteroid completes one rotation every 2.26 hours, a spin rate fast enough to influence its shape — likely giving rise to the equatorial ridge observed in radar images. This top-like morphology, shared with several other rapidly rotating asteroids, suggests mass redistribution over time and points to a delicate gravitational balance at the surface. Such loosely bound “rubble pile” structures are common in near-Earth objects and pose significant challenges in deflection scenarios: too much force could fragment the body rather than shift its trajectory, complicating mitigation outcomes. Understanding Didymos's internal composition and structural stability is essential for modeling how similar bodies would respond to kinetic or nuclear deflection methods.
    <br><br>
    Read More: <a href=https://science.nasa.gov/solar-system/asteroids/didymos/">https://science.nasa.gov/solar-system/asteroids/didymos/</a>
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
            "name": "Phaethon",
            "slug": "3200_phaethon",
            "desc": """
    Asteroid 3200 Phaethon occupies a unique position in planetary defense discussions due to its highly eccentric orbit, unexpected activity near the Sun, and its role as the parent body of the Geminid meteor shower. At approximately 5.4 kilometers wide, Phaethon is larger than most near-Earth objects typically associated with meteor showers. While its current orbit does not pose an immediate impact risk, Phaethon is classified as a potentially hazardous asteroid due to its size and its Earth-crossing trajectory. Given its extreme solar exposure, highly elongated orbit, and dynamic behavior, Phaethon represents a complex object that could evolve unpredictably over time (NASA, 2023).
    <br><br>
    One of the primary concerns regarding Phaethon is its apparent structural instability. Though initially believed to be a dormant, dust-shedding asteroid, new evidence from NASA’s SOHO and STEREO missions indicates that Phaethon’s comet-like tail is not made of dust, but of vaporized sodium gas released from its surface under extreme heat. This suggests that Phaethon may be experiencing internal stress or volatile-driven activity, even without ice — challenging assumptions about what triggers mass loss in small bodies. The presence of a large meteoroid stream (the Geminids), which Phaethon alone cannot replenish in its current state, strongly implies that a major surface disruption occurred in the recent past, possibly from rapid rotation or thermal fracturing. If such an event were to recur, it could alter Phaethon’s trajectory or produce hazardous debris fields in Earth’s orbital path.
    <br><br>
    Read More: <a href="https://www.nasa.gov/solar-system/asteroids-comet-like-tail-is-not-made-of-dust-solar-observatories-reveal/">https://www.nasa.gov/solar-system/asteroids-comet-like-tail-is-not-made-of-dust-solar-observatories-reveal/</a>
    """
        },
    ]

    return asteroid_data