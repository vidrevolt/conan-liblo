#include <iostream>

// LibLo (OSC)
#include <lo/lo.h>
#include <lo/lo_cpp.h>

int main() {
    lo::ServerThread st(9000);
    st.is_valid();
}
