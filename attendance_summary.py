import os
import pandas as pd
from datetime import datetime, time
import zipfile

def extract_csv_files(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted CSV files to {extract_to}")

def parse_time(time_str):
    try:
        return datetime.strptime(time_str, "%m/%d/%y, %I:%M:%S %p").time()
    except ValueError:
        return time(0, 0)  # Default to 00:00 if parsing fails

def process_csv_files(folder_path, class_start, class_end, late_threshold):
    student_data = []
    print(f"Processing CSV files in {folder_path}...")

    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            print(f"Reading file: {file_path}")

            with open(file_path, 'r') as file:
                content = file.read()
                print(f"Content preview: {content[:1000]}")  # Preview the first 1000 characters

                sections = content.split('\n\n')
                for section in sections:
                    if '2. Participants' in section:
                        lines = section.split('\n')
                        if not lines or len(lines) < 2:
                            continue  # Skip if there's no valid content
                        
                        header_line = lines[0]
                        headers = header_line.split(',')
                        print(f"Headers: {headers}")  # Debugging header information
                        
                        name_idx = headers.index('Name') if 'Name' in headers else -1
                        email_idx = headers.index('In-Meeting Email') if 'In-Meeting Email' in headers else -1
                        join_idx = headers.index('First Join') if 'First Join' in headers else -1
                        leave_idx = headers.index('Last Leave') if 'Last Leave' in headers else -1
                        
                        print(f"Column indices - Name: {name_idx}, Email: {email_idx}, Join: {join_idx}, Leave: {leave_idx}")

                        for line in lines[1:]:
                            if line.strip():
                                fields = line.split(',')
                                if len(fields) < max(name_idx, email_idx, join_idx, leave_idx) + 1:
                                    print(f"Skipping line due to insufficient fields: {line}")
                                    continue  # Skip if there are not enough fields
                                
                                name = fields[name_idx].strip() if name_idx != -1 else ''
                                email = fields[email_idx].strip() if email_idx != -1 else ''
                                join_time = parse_time(fields[join_idx].strip()) if join_idx != -1 else time(0, 0)
                                leave_time = parse_time(fields[leave_idx].strip()) if leave_idx != -1 else time(0, 0)

                                print(f"Processing - Name: {name}, Email: {email}, Join: {join_time}, Leave: {leave_time}")  # Debugging data

                                if name and email:
                                    student_data.append({
                                        'Student Name': name,
                                        'ID/E-mail': email,
                                        'Attended Sessions': 0,
                                        'Absent Sessions': 0,
                                        'Late Sessions': 0,
                                    })

                                    student = next((item for item in student_data if item['Student Name'] == name), None)
                                    if student:
                                        if join_time <= class_end and leave_time >= class_start:
                                            student['Attended Sessions'] += 1
                                            if join_time > late_threshold:
                                                student['Late Sessions'] += 1
                                        else:
                                            student['Absent Sessions'] += 1

    print(f"Student data processed: {student_data}")
    return student_data

def generate_report(student_data, output_file):
    try:
        df = pd.DataFrame(student_data)
        df.to_csv(output_file, index=False)
        print(f"Report successfully generated at: {output_file}")
    except PermissionError as e:
        print(f"PermissionError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    zip_path = "C:/Users/User/source/repos/CE2709/miniProject/attendance_dummy_data.zip"
    extract_folder = "attendance_data"
    
    # Extract CSV files from the zip
    extract_csv_files(zip_path, extract_folder)
    
    # Set class time and late threshold
    class_start = time(9, 0)  # 9:00 AM
    class_end = time(10, 30)  # 10:30 AM
    late_threshold = time(9, 10)  # 9:10 AM

    student_data = process_csv_files(extract_folder, class_start, class_end, late_threshold)
    generate_report(student_data, "attendance_summary_report.csv")
    print("Attendance summary report generated: attendance_summary_report.csv")

if __name__ == "__main__":
    main()
