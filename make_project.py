from pathlib import Path

class DirectoryManager:
    def __init__(self, base_dir, dir_name):
        """
        初始化目录管理器
        :param base_dir: 父目录路径
        :param dir_name: 要创建的目录名称
        """
        self.base_dir = Path(base_dir)
        self.dir_name = dir_name
        self.target_dir = self.base_dir / dir_name

    def create_directory(self):
        """
        创建目标目录
        """
        if not self.target_dir.exists():
            self.target_dir.mkdir(parents=True, exist_ok=True)
            print(f"目录 '{self.target_dir}' 创建成功。")
        else:
            print(f"目录 '{self.target_dir}' 已存在。")

    def create_files_with_content(self, file_content_dict):
        """
        在目标目录下创建文件并写入指定内容
        :param file_content_dict: 文件名到内容的映射字典
        """
        for file_name, content in file_content_dict.items():
            file_path = self.target_dir / file_name
            with open(file_path, "w") as f:
                f.write(content)
            print(f"文件 '{file_path}' 创建成功，并写入内容。")


if __name__ == "__main__":
    # 示例用法
    base_directory = "D:/example"  # 指定父目录路径
    directory_name = "test"  # 指定要创建的目录名称

    # 指定每个文件的内容
    file_content_dict = {
        "test.in": "This is the input file content.",
        "test.out": "This is the output file content.",
        "test.cpp": "#include <iostream>\nint main() { std::cout << \"Hello, World!\"; return 0; }",
        "test.txt": "This is an additional text file."
    }

    # 创建目录管理器实例
    manager = DirectoryManager(base_directory, directory_name)
    manager.create_directory()  # 创建目录
    manager.create_files_with_content(file_content_dict)  # 创建文件并写入内容