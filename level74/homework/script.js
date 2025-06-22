function rounding(n, m) {
    const lower = Math.floor(n / m) * m;
    const upper = lower + m;

    if (n - lower === upper - n) {
        return n;
    }

    return (n - lower < upper - n) ? lower : upper;
  
  
}