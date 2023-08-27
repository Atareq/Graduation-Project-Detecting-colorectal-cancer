import joblib
import pandas as pd
from .forms import TestForm


# Load the trained model from the pickle file
test_file_path = (
        "//media//a//DATA//Fathy_code//graduation_project//cancer_detect_app//test.txt"
    )
input_data = (
            "Age\tGender\tBMI\tFOBT\tDiabetes\tVegetarian\tSmoking\tLibrary_Size_Wirbel\t"
            "Library_Size_raw\tLibrary_Size_filtered\tLocalization_L\tLocalization_L,R\t"
            "Localization_L,RM\tLocalization_R\tLocalization_RM\tLocalization_RM, L,R\n")

pkl_path = (
    "//media//a//DATA//Fathy_code//graduation_project//cancer_detect_app//model_file.pkl")

def ml_result(form):
    prepro_input(form)
    loaded_model = joblib.load(pkl_path)
    # Retrieve form data
    final_test_data  = pd.read_csv(test_file_path, sep='\t')
    result = loaded_model.predict(final_test_data)
    return result


def prepro_input(data):
    if data["sample_taken"] == ("left colon"):
        sample_taken = ['\t' +  "1" + '\t' +   "0"  + '\t' + "0" + '\t' +  "0" + '\t' +   "0" + '\t' +  "0"]
    elif data["sample_taken"] == ('Right colon'):
        sample_taken = ['\t' +  "0" + '\t' +   "1" + '\t' +  "0" + '\t' +  "0" + '\t' +  "0"  + '\t' + "0"]
    elif data["sample_taken"] == ('Rectum'):
        sample_taken = ['\t' +  "0"  + '\t' +  "0" + '\t' +  "1" + '\t' +  "0" + '\t' +   "0" + '\t' +  "0"]
    elif data["sample_taken"] == ('left and right colon and rectum'):
        sample_taken = ['\t' +  "0"  + '\t' +  "0" + '\t' +  "0" + '\t' +  "1" + '\t' +  "0" + '\t' +  "0"]
    elif data["sample_taken"] == ('left and right colon'):
        sample_taken = ['\t' +  "0"   + '\t' + "0" + '\t' +  "0"  + '\t' + "0" + '\t' +  "1" + '\t' +  "0"]
    else:
        sample_taken = [ '\t' +"0" + '\t' +  "0"  + '\t' + "0" + '\t' +  "0"  + '\t' + "0" + '\t' +  "1"]
    # Prepare the data for writing

    file_data = (
        str(data['age']) + '\t' + str(data['gender']) + '\t' + str(data['bmi']) + '\t' +
        str(data['fobt']) + '\t' + str(data['diabetes']) + '\t' + str(data['vegetarian']) + '\t' +
        str(data['smoking']) + '\t' + str(data['library_size_wirbel']) + '\t' +
        str(data['library_size_raw']) + '\t' + str(data['library_size_filtered']) + 
        '\t'.join(sample_taken)
    )


    # Open the file in write mode
    with open(test_file_path, "w") as test_file:
            # Write the new content
        test_file.write(input_data + file_data)
        
    x=turn_to_num()
    return x
def turn_to_num():

    test_data = pd.read_csv(test_file_path, sep='\t')

    test_data['Gender'] = test_data['Gender'].replace({'female': '1', 'male': '0'})
    test_data['FOBT'] = test_data['FOBT'].replace({'positive': '1', 'negative': '0'})

    test_data = test_data.replace({'Yes': '1', 'No': '0'})

    # Open the file in write mode ("w")
    with open(test_file_path, "w") as file:
    # Write the updated content to the file
     file.write(test_data.to_csv(index=False, sep='\t'))
