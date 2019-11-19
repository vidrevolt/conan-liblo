from conans import ConanFile, CMake, tools
import os


class LibLoConan(ConanFile):
    name = "liblo"
    description = "An implementation of the Open Sound Control protocol for POSIX systems"
    topics = ("conan", "liblo", "osc")
    url = "https://github.com/vidrevolt/conan-liblo"
    homepage = "http://liblo.sourceforge.net/"
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    no_copy_source = True

    _source_subfolder = "liblo"
    _build_subfolder = "build"

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(
                source_folder=os.path.join(self._source_subfolder, "cmake"),
                build_folder=self._build_subfolder)
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="lo/*.h", dst="include", src=self._source_subfolder)
        self.copy(pattern="*.dll", dst="bin", keep_path=False)
        self.copy(pattern="*.lib", dst="lib", keep_path=False)
        self.copy(pattern="*.a", dst="lib", keep_path=False)
        self.copy(pattern="*.so*", dst="lib", keep_path=False)
        self.copy(pattern="*.dylib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
