#v.2: simplified
from pathlib import Path

def create_folder_structure():
    """Create the recommended DS 2001 folder structure."""

    project_dir = Path.cwd()
    print(project_dir)

    weeks = [f'week{i}' for i in range(1, 11)]
    weeks.append('week11-14')

    for week in weeks:
        week_dir = project_dir / week
        week_dir.mkdir(exist_ok=True)

        if week == 'week11-14':
            project_folder = week_dir / 'project'
            project_folder.mkdir(exist_ok=True)
        else:
            assignment_file = week_dir / f'assignment{week[-1]}.py'
            other_files_dir = week_dir / 'other_files'
            other_files_dir.mkdir(exist_ok=True)
            assignment_file.touch()

    print(f'DS 2001 folder structure created in {project_dir}')

if __name__ == '__main__':
    create_folder_structure()
