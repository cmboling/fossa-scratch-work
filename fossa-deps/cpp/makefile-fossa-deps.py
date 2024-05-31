import re
import yaml

def parse_makefile(makefile_path):
    with open(makefile_path, 'r') as file:
        makefile_content = file.read()
    return makefile_content

def extract_dependencies(makefile_content):
    lib_path_pattern = re.compile(r'LIB_PATH\s*=\s*(.*)')
    inc_path_pattern = re.compile(r'INC_PATH\s*=\s*(.*)')

    lib_paths = lib_path_pattern.search(makefile_content)
    inc_paths = inc_path_pattern.search(makefile_content)

    if lib_paths:
        lib_paths = lib_paths.group(1).split()
    else:
        lib_paths = []

    if inc_paths:
        inc_paths = inc_paths.group(1).split()
    else:
        inc_paths = []

    return lib_paths, inc_paths

def create_fossa_deps(lib_paths, inc_paths, output_path):
    vendored_dependencies = []

    for path in lib_paths + inc_paths:
        dependency_name = path.split('/')[-1]
        vendored_dependencies.append({
            'name': dependency_name,
            'path': path,
            'version': 'unknown'  # Version info is not available in the Makefile
        })

    fossa_deps = {'vendored-dependencies': vendored_dependencies}

    with open(output_path, 'w') as file:
        yaml.dump(fossa_deps, file, default_flow_style=False)

if __name__ == "__main__":
    makefile_path = 'Makefile'  # Path to your Makefile
    output_path = 'fossa-deps.yml'  # Path to the output FOSSA dependencies file

    makefile_content = parse_makefile(makefile_path)
    lib_paths, inc_paths = extract_dependencies(makefile_content)
    create_fossa_deps(lib_paths, inc_paths, output_path)

    print(f'FOSSA dependencies written to {output_path}')
