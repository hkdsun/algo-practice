def is_happy(n)
  res = 0
  while n > 0
    res += (n % 10)**2
    n = n / 10
  end
  if res == 1
    return true
  else
    return is_happy(res)
  end
end
