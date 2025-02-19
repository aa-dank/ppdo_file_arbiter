from label_arbiter.labeling.labeler import Labeler

def main(file_path):
    labeler = Labeler()
    labels = labeler.label_file(file_path)
    print(f\"Predicted labels: {labels}\")

if __name__ == \"__main__\":
    test_file = \"data/test_files/sample.pdf\"
    main(test_file)