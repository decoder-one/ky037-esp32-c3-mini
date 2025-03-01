# ky037-esp32-c3-mini

Im Internet finden sich ausschließlich nicht funktionierende Programme in C oder Python für Microprozessoren mit dem Audiosensor ky037. Nutzer berichten,
dass der Sensor offenbar defekt oder von schlechter Qualität ist. Die Feineinstellung (Rädchen) auf dem Sensor soll nicht funktionieren.

Ich habe den Sensor anders verkabelt und habe Erfolg gehabt. Vielleicht sind auch digital und alaloger Ausgang falsch gekennzeichnet? Sowohl mit der analoge als auch digitalen Verkabelung kann man bei richtiger Einstellung der Empfindlichkeit gute Ergebnisse erzielen.

Die Verkabelung steht im Code. Ich habe hier mit einem esp32-c3 mini experimentiert.

