from Stemmingrules import rules as stemm

def save_file(data):
    with  open("C:\Users\Faisal Khan\.astah\Desktop\Semester-8\NLP\Assignments\Assignment-1\output.txt", 'r') as file:
        for word in data:
            file.write(word + '\n')

def load_file(file_name):
    data = []
    with  open("C:\Users\Faisal Khan\.astah\Desktop\Semester-8\NLP\Assignments\Assignment-1\input.txt", 'r') as file:
        for line in file:
            data.append(line.strip('\n|.|:|\(|\)').replace(' ',',').split(','))
    return data

if __name__ == '__main__':


    data = load_file("input.txt")
    out = open("C:\Users\Faisal Khan\.astah\Desktop\Semester-8\NLP\Assignments\Assignment-1\output.txt", 'w')
    steps = stemm()
    vocab = totalwor = 0
    for word_list in data:
        for word in word_list:
            word = word.strip('(|)|.|?')
            check = word
            stem = steps.step1a(word)
            stem = steps.step1b(stem)
            stem = steps.step1c(stem)
            stem = steps.step2(stem)
            stem = steps.step4(stem)
            stem = steps.step5a(stem)
            stem = steps.step5b(stem)
            totalwor += 1
            if (check != stem):
                out.write(word+" --> "+ stem + '\n')
                vocab += 1
            
    print("Total word is ",totalwor, " vocabulary size is ",vocab)
    
    print("Words affected by step-1", steps.step_res('st-1'))
    print("Words affected by step-2",steps.step_res('st-2'))
    print("Words affected by step-3",steps.step_res('st-3'))
    print("Words affected by step-4",steps.step_res('st-4'))
    print("Words affected by step-5",steps.step_res('st-5'))
