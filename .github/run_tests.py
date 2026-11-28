import os
import sys
import subprocess
 

 
folder = ".github"
programsFolder = os.path.join(folder, "programs")
 
 
def runFuzzer(fuzzArgs):
    command = ["python3", "src/fuzz.py"] + fuzzArgs
    result = subprocess.run(command, capture_output=True, text=True)
    return " ".join(command), result.stdout, result.stderr
 
 
def importantLines(output):
    keep = []
    for line in output.splitlines():
        if "EXCEPTION" in line or line.startswith("DONE"):
            keep.append(line)
    return keep
 
 
def printTotals(passCount, failCount):
    print("==============================")
    print("TOTAL: " + str(passCount + failCount))
    print("PASSED: " + str(passCount))
    print("FAILED: " + str(failCount))
    print("==============================")
 
 
def fixedTests():
    passCount = 0
    failCount = 0
    for program in sorted(os.listdir(programsFolder)):
        name = program[:-3]  
        setsFolder = os.path.join(folder, "fixed_inputs", name)
        if not os.path.isdir(setsFolder):
            continue
        for setName in sorted(os.listdir(setsFolder)):
            seedPath = os.path.join(setsFolder, setName)
            command, output, errorText = runFuzzer([os.path.join(programsFolder, program), seedPath, "--budget", "0"])
            print("$ " + command)
 
            file = open(os.path.join(folder, "fixed_expected", name, setName + ".txt"))
            expected = file.read().strip().splitlines()
            file.close()
            actual = output.strip().splitlines()
 
            testName = program + " / " + setName
            if actual == expected:
                print("[PASS] " + testName)
                passCount += 1
            else:
                print("[FAIL] " + testName + ": output mismatch")
                if errorText:
                    print(errorText)
                failCount += 1
    printTotals(passCount, failCount)
    return failCount
 
 
def bugTests():
    passCount = 0
    failCount = 0
    for program in sorted(os.listdir(programsFolder)):
        name = program[:-3]
        seedPath = os.path.join(folder, "campaign_seeds", name)
 
        file = open(os.path.join(folder, "campaign_expected", name + ".txt"))
        wantedErrors = []
        for line in file.read().splitlines():
            if line.strip() != "":
                wantedErrors.append(line.strip())
        file.close()
 
        outputs = []
        for randomSeed in ["0", "1", "2"]:
            label = program + " seed=" + randomSeed + ": "
            command, output, errorText = runFuzzer([os.path.join(programsFolder, program), seedPath,
                                                    "--budget", "15000", "--seed", randomSeed])
            print(label + "$ " + command)
            for line in importantLines(output):
                print(label + line)
            outputs.append(output)
 
        allFound = True
        results = []
        for wanted in wantedErrors:
            foundCount = 0
            for output in outputs:
                if "EXCEPTION " + wanted + " input=" in output:
                    foundCount += 1
            results.append(wanted + " found in " + str(foundCount) + "/3 campaigns")
            if foundCount < 2:
                allFound = False
 
        if allFound:
            print("[PASS] " + program + ": " + "; ".join(results))
            passCount += 1
        else:
            print("[FAIL] " + program + ": " + "; ".join(results))
            failCount += 1
    printTotals(passCount, failCount)
    return failCount
 
 
def randomBaseline():
    for program in sorted(os.listdir(programsFolder)):
        name = program[:-3]
        seedPath = os.path.join(folder, "campaign_seeds", name)
        label = program + " random seed=0: "
        command, output, errorText = runFuzzer([os.path.join(programsFolder, program), seedPath,
                                                "--budget", "15000", "--seed", "0", "--random"])
        print(label + "$ " + command)
        for line in importantLines(output):
            print(label + line)
    return 0
 
 
if __name__ == "__main__":
    step = sys.argv[1]
    if step == "fixed":
        failCount = fixedTests()
    elif step == "bugs":
        failCount = bugTests()
    else:
        failCount = randomBaseline()
    if failCount > 0:
        sys.exit(1)
 
