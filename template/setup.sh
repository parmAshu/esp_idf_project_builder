# Get the project directory path
project_path=$(pwd)
idf_path=$project_path/esp-idf
tools_path=$project_path/tools

# Print the paths to console
echo "PROJECT PATH"
echo $project_path
echo "ESP IDF PATH"
echo $idf_path
echo "TOOLS PATH"
echo $tools_path

export IDF_PATH=$idf_path
export IDF_TOOLS_PATH=$tools_path
export PATH=$idf_path/tools:$PATH

source $idf_path/export.sh