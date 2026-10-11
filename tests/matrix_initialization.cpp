#include <algorithm>
#include <cassert>
#include <cmath>
#include <limits>

#include "densematrix.h"

int main() {
  for (int rows : {1, 6, 106}) {
    for (unsigned int threads : {1, 2, 8, 10, 12}) {
      fasttext::DenseMatrix matrix(rows, 8);
      std::fill(matrix.data(), matrix.data() + rows * 8,
                std::numeric_limits<fasttext::real>::quiet_NaN());
      matrix.uniform(0.125, threads, 0);
      for (int i = 0; i < rows * 8; ++i) {
        assert(std::isfinite(matrix.data()[i]));
        assert(std::abs(matrix.data()[i]) <= 0.125);
      }
    }
  }
}
