use pyo3::prelude::*;

#[pyfunction]
#[pyo3(text_signature = "(a, b, /)")]
pub fn concat_strings(a: String, b: String) -> PyResult<String> {
    Ok(a + &b)
}

