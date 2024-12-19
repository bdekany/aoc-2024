const fs = require('fs');
const readline = require('readline');

// Chemin vers ton fichier
const filePath = 'puzzle-input.txt';

// Variable Globale pour les résultats finaux
let resultat_part1 = 0;
let resultat_part2 = 0;

// Le rule Book
let rulebook = {}

// Créer l'interface de lecture
const readInterface = readline.createInterface({
    input: fs.createReadStream(filePath),
    // output: process.stdout,
    console: false
});

// Boucler sur chaque ligne du fichier
readInterface.on('line', function(line) {
    if (line.indexOf('|') != -1) {
        let rule = line.split("|");
        if ( ! Object.hasOwn(rulebook, rule[0]) ) [
            rulebook[rule[0]] = []
        ]
        rulebook[rule[0]].push(rule[1])

    }
    
    // Part 1
    if (line.indexOf(',') != -1) {

        let found = ""
        let redflag = 0

        update = line.split(",")
        while (update.length > 0) {
            page = update.pop()
            if (Object.hasOwn(rulebook, page)) {
                found =  update.filter((val, index) => {
                    return rulebook[page].includes(val)
                })
                if ( found.length > 0 ) {
                    redflag = 1
                }
            }
        }

        if ( redflag == 0 ) {  // Part 1
            update = line.split(",")
            //console.log("serie valide: ", update)
            index = Math.floor(update.length / 2)
            resultat_part1 += parseInt(update[index])
        } else {     // Part 2
            update = line.split(",")
            update.sort((a, b) => {
                if (! Object.hasOwn(rulebook, a)) {
                    return 0
                }
                if (rulebook[a].includes(b)) {
                    return -1
                } else {
                    return 0
                }
            })
            console.log("new:", update)
            index = Math.floor(update.length / 2)
            resultat_part2 += parseInt(update[index])
        }
    }

    // Part 2
    resultat_part2 += 0

});

// Gestion de la fin de fichier
readInterface.on('close', function() {
    console.log('Lecture du fichier terminée.');
    console.log('===== Resulat Day 5 ======');
    console.log('Part 1:' + resultat_part1);
    console.log('Part 2:' + resultat_part2);
});