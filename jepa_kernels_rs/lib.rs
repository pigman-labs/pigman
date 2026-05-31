pub fn cosine_distance(a: &[f32], b: &[f32]) -> Option<f32> {
    if a.len() != b.len() {
        return None;
    }

    let mut dot = 0.0;
    let mut norm_a = 0.0;
    let mut norm_b = 0.0;

    for (x, y) in a.iter().zip(b.iter()) {
        dot += x * y;
        norm_a += x * x;
        norm_b += y * y;
    }

    if norm_a == 0.0 || norm_b == 0.0 {
        return Some(1.0);
    }

    Some(1.0 - dot / (norm_a.sqrt() * norm_b.sqrt()))
}

pub fn l2_norm(a: &[f32]) -> f32 {
    a.iter().map(|x| x * x).sum::<f32>().sqrt()
}

pub fn dot(a: &[f32], b: &[f32]) -> Option<f32> {
    if a.len() != b.len() {
        return None;
    }
    Some(a.iter().zip(b.iter()).map(|(x, y)| x * y).sum())
}

#[cfg(test)]
mod tests {
    use super::cosine_distance;

    #[test]
    fn identical_vectors_have_zero_distance() {
        assert_eq!(cosine_distance(&[1.0, 0.0], &[1.0, 0.0]), Some(0.0));
    }

    #[test]
    fn dot_product_works() {
        assert_eq!(super::dot(&[1.0, 2.0], &[3.0, 4.0]), Some(11.0));
    }

    #[test]
    fn l2_norm_works() {
        assert_eq!(super::l2_norm(&[3.0, 4.0]), 5.0);
    }
}
