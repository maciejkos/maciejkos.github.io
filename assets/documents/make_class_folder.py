from pathlib import Path
import os

def create_folder_structure():
    """Create the recommended DS 2001 folder structure."""
    home_dir = Path.home()

    if os.name == 'posix':  # macOS
        project_dir = home_dir / 'Projects' / 'ds2001'
    else:  # Windows
        project_dir = home_dir / 'Documents' / 'ds2001'

    project_dir.mkdir(parents=True, exist_ok=True)

    weeks = [f'week{i}' for i in range(1, 15)]
    weeks.extend(['week11-12', 'week14'])

    for week in weeks:
        week_dir = project_dir / week
        week_dir.mkdir(exist_ok=True)

        if week == 'week11-12':
            project_folder = week_dir / 'project'
            project_folder.mkdir(exist_ok=True)
        elif week == 'week14':
            presentation_folder = week_dir / 'project_presentation'
            presentation_folder.mkdir(exist_ok=True)
        else:
            assignment_file = week_dir / f'assignment{week[-1]}.py'
            other_files_dir = week_dir / 'other_files'
            other_files_dir.mkdir(exist_ok=True)
            assignment_file.touch()

    print(f'DS 2001 folder structure created in {project_dir}')

if __name__ == '__main__':
    create_folder_structure()