// // use ndarray::{Array, Array2};
// // use ndarray_linalg::Eigen;
// // use num_complex::Complex;
// use pyo3::prelude::*;

// #[pyclass]
// struct ComplexMatrix {
//     data: Array2<Complex<f64>>,
// }

// #[pymethods]
// impl ComplexMatrix {
//     #[new]
//     fn new(data: Array2<Complex<f64>>) -> Self {
//         ComplexMatrix { data }
//     }

//     fn eigenvalues(&self) -> Vec<Complex<f64>> {
//         Eigen::eigenvalues(&self.data).unwrap()
//     }
// }
