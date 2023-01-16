# quippers
Mixed Rust/Python project for QIP
This tool is used for learning how to use Rust functions in Python code.

## Quick Start
Create a virtual environment and install maturin:
```bash
python3 -m venv .env
source .env/bin/activate
pip install maturin
```

To write a Rust function, create a new file in the `src` directory. We use `#[pyfunction]` and `#[pymodule]` to expose the function to the Python module. For example, `src/lib.rs`:
```rust
use pyo3::prelude::*;
...
#[pyfunction]
fn add_in_rust(a: i32, b: i32) -> PyResult<i32> {
    Ok(a + b)
}
...
#[pymodule]
fn quippers(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(add_in_rust, m)?)?;
    Ok(())
}
```

Then, build the Rust code:
```bash
maturin develop
```
Alternatively, use `maturin build` to build a wheel file (I don't fully understand the technical differences between the two yet).

To use the Rust function in Python, import the module and call the function:
```python
import quippers
quippers.add_in_rust(1, 2)
```

### Notes
- Design should minimize the number of times data is passed back and forth between the two languages
- Type conversions are handled by PyO3 (?) https://pyo3.rs/v0.16.4/conversions/tables.html?

## Resources
- https://github.com/PyO3/pyo3
- https://www.maturin.rs/project_layout.html
- https://www.infoworld.com/article/3664124/how-to-use-rust-with-python-and-python-with-rust.html
- https://medium.com/qiskit/new-weve-started-using-rust-in-qiskit-for-better-performance-a3676433ca8c
