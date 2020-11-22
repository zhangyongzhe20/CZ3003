Project Requirements
The Teaching, Learning and Pedagogy Division (TLPD) of NTU is attempting to introduce a social game to gamify and socialize teaching and learning of software engineering courses. Students can learn and compete with each other via playing the game, and teachers can assess the mastery of course via data analysis.
The game shall have a theme (e.g., castle conquer), and have different characters for players to choose. The game shall consist of a series of worlds to be explored (i.e., representing different phases of the life cycle of software engineering, ranging from requirements engineering and architectural design to implementation and software testing). Each world shall have several sections (i.e., representing specific topics of each phase from basic ones to advanced ones), and each section has several levels (i.e., representing questions relevant to specific topics with increasing difficulties). Further, the game shall have a leaderboard to keep the players engaged for higher ranks.
Note: you shall design your own theme in your game and use open source game engines.
The game shall support game data analysis in two aspects.
• First, the game shall analyze each player’s playing history to continuously obtain the student’s mastery of the course in real-time. Based on this real-time analysis results, the questions of the following levels can be customized. For example, if a player has a good command of the course according to the playing history, the player shall deal with more difficult questions when playing the game.
• Second, the game shall analyze all the players’ playing history to continuously obtain the overall mastery of the course in real time, and produce a summary report for the teachers (including which parts are well-mastered by the students, and which parts are not). Based on this report, teachers can logically adjust the teaching contents and key points during the classroom teaching.
The game shall allow players to design their own levels so that students can challenge with each other and teachers can give assignments to students through social media (e.g., Facebook and Twitter).
Note: you shall provide two or more social media in your game.
Non-functional requirements need to be considered in the project.
Design your system to consider one and only one of the following non-functional requirements must to be considered in the project.
Flexibility, Maintainability, Performance, Reusability, Robustness, Reliability or Security.
For example, performance requirements could be:
The game must support at least 100 simultaneously online players. The response time for displaying the scenario must be less than 1 second. Players’ answers must be submitted within 1 second.


Lead the backend team to build server in Django and check more docs in the backend folder.
