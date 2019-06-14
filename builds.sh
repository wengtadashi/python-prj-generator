echo "Make a directory for prj:"
read directory
if [ -d "${directory}" ]; then
    echo "${directory} exists!"
    exit 1
fi
if [ -z "${directory}" ]; then
    echo "Enter a directory name."
    exit 1
fi
mkdir "${directory}"
docker build -t au .
docker run --mount type=bind,source="$(pwd)"/outputs,target=/tmp/sre/outputs --rm -i au python main.py
mv ./outputs/* "${directory}"
