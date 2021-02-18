#!/usr/bin/env python3

import sys
import argparse
import csv
import array

class SpellTome:
    inputCSVFileName = ''
    outputCSVFileName = ''
    
    spells = {
            'level' : [],
            'name' : [],
            'description' : [],
            'school' : [],
            'duration' : [],
            'range' : [],
            'savingThrow' : [],
            'spellResistance' : [],
            'url' : []
            }

    def __init__(self, inputCSVFileName, outputCSVFileName):
        self.inputCSVFileName = inputCSVFileName
        self.outputCSVFileName = outputCSVFileName

    def GenerateNewTomeFile(self):
        self.populateSpells()
        self.writeTomeCSV()

    def populateSpells(self):
        print("Populating Spell Tome")
        self.spells['name'] = self.getNames()
        self.spells['url'] = self.getUrls()

    def writeTomeCSV(self):
        print("Writing Spell Tome")
        with open(self.outputCSVFileName, "x", newline='') as outputCSVFile:
            csvwriter = csv.writer(outputCSVFile, dialect='excel');
            for i in range(len(self.spells['name'])):
                csvwriter.writerow([
                    self.spells['name'][i],
                    self.spells['url'][i]
                    ])
        print("Tome Written!")

    def getNames(self):
        spellNames = []
        with open(self.inputCSVFileName, newline='') as inputCSVFile:
            csvreader = csv.reader(inputCSVFile)
            for row in csvreader:
                spellNames.append(row[0])
        return spellNames

    def getUrls(self):
        urls = []
        for spell in self.spells["name"]:
            spell = kebabCase(spell)
            url = 'https://www.d20pfsrd.com/magic/all-spells/'
            url += spell[0] + '/'
            url += spell
            urls.append(url)
        return urls

def kebabCase(string):
    string = string.lower()
    string = string.replace(" ", "-")
    return string

def main():
    inputCSVFileName = sys.argv[1]
    outputCSVFileName = sys.argv[2]
    
    spelltome = SpellTome(inputCSVFileName, outputCSVFileName)
    spelltome.GenerateNewTomeFile()

if __name__ == "__main__":
    main()
