import lodash as _
import unittest

class TestArrayMethods(unittest.TestCase):
  def test_chunk(self):
    self.assertEqual(_.chunk(['a', 'b', 'c', 'd'], 2), [['a', 'b'], ['c', 'd']])
    self.assertEqual(_.chunk(['a', 'b', 'c', 'd'], 3), [['a', 'b', 'c'], ['d']])

  def test_compact(self):
    self.assertEqual(_.compact([0, 1, False, 2, '', 3]), [1, 2, 3])

  def test_concat(self):
    self.assertEqual(_.concat([1], 2, [3], [[4]]), [1, 2, 3, [4]])

  def test_difference(self):
    self.assertEqual(_.difference([2, 1], [2, 3]), [1])
  
  def test_differenceBy(self):
    self.assertEqual(_.differenceBy([2.1, 1.2], [2.3, 3.4], _.floor), [1.2])

  def test_drop(self):
    self.assertEqual(_.drop([1, 2, 3]), [2, 3])
    self.assertEqual(_.drop([1, 2, 3], 2), [3])
    self.assertEqual(_.drop([1, 2, 3], 5), [])
    self.assertEqual(_.drop([1, 2, 3], 0), [1, 2, 3])

  def test_dropRight(self):
    self.assertEqual(_.dropRight([1, 2, 3]), [1, 2])
    self.assertEqual(_.dropRight([1, 2, 3], 2), [1])
    self.assertEqual(_.dropRight([1, 2, 3], 5), [])
    self.assertEqual(_.dropRight([1, 2, 3], 0), [1, 2, 3])

  def test_dropRightWhile(self):
    array = [
      { 'user': 'barney',  'active': True },
      { 'user': 'fred',    'active': False },
      { 'user': 'pebbles', 'active': False }
    ]
    _.dropRightWhile(array, lambda o: not o['active'])
    self.assertEqual(array, [{ 'user': 'barney', 'active': True }])

  def test_dropWhile(self):
    array = [
      { 'user': 'barney',  'active': False },
      { 'user': 'fred',    'active': False },
      { 'user': 'pebbles', 'active': True }
    ]
    _.dropWhile(array, lambda o: not o['active'])
    self.assertEqual(array, [{ 'user': 'pebbles', 'active': True }])

  def test_fill(self):
    self.assertEqual(_.fill([1, 2, 3], 'a'), ['a', 'a', 'a'])
    self.assertEqual(_.fill([4, 6, 8, 10], '*', 1, 3), [4, '*', '*', 10])

  def test_findIndex(self):
    users = [
      { 'user': 'barney',  'active': False },
      { 'user': 'fred',    'active': False },
      { 'user': 'pebbles', 'active': True }
    ]
    self.assertEqual(_.findIndex(users, lambda o: o['user'] == 'barney'), 0)
    self.assertEqual(_.findIndex(users, lambda o: o['user'] == 'fred' and not o['active']), 1)
    self.assertEqual(_.findIndex(users, lambda o: not o['active']), 0)
    self.assertEqual(_.findIndex(users, lambda o: o['active']), 2)

  def test_findLastIndex(self):
    users = [
      { 'user': 'barney',  'active': True },
      { 'user': 'fred',    'active': False },
      { 'user': 'pebbles', 'active': False }
    ]
    self.assertEqual(_.findLastIndex(users, lambda o: o['user'] == 'pebbles'), 2)
    self.assertEqual(_.findLastIndex(users, lambda o: o['user'] == 'barney' and o['active']), 0)
    self.assertEqual(_.findLastIndex(users, lambda o: not o['active']), 2)
    self.assertEqual(_.findLastIndex(users, lambda o: o['active']), 0)

  def test_flatten(self):
    array = [1, [2, [3, [4]], 5]]
    self.assertEqual(_.flatten(array), [1, 2, [3, [4]], 5])

  def test_flattenDeep(self):
    array = [1, [2, [3, [4]], 5]]
    self.assertEqual(_.flattenDeep(array), [1, 2, 3, 4, 5])
  
  def test_flattenDepth(self):
    array = [1, [2, [3, [4]], 5]]
    self.assertEqual(_.flattenDepth(array), [1, 2, [3, [4]], 5])
    self.assertEqual(_.flattenDepth(array, 2), [1, 2, 3, [4], 5])

  def test_fromPairs(self):
    self.assertEqual(_.fromPairs([['a', 1], ['b', 2]]), { 'a': 1, 'b': 2 })

  def test_head(self):
    self.assertEqual(_.head([1, 2, 3]), 1)

  def test_indexOf(self):
    self.assertEqual(_.indexOf([1, 2, 1, 2], 2), 1)
    self.assertEqual(_.indexOf([1, 2, 1, 2], 2, 2), 3)

  def test_initial(self):
    self.assertEqual(_.initial([1, 2, 3]), [1, 2])

  def test_intersection(self):
    self.assertEqual(_.intersection([1, 2], [1, 3], [1, 4]), [1])

  def test_join(self):
    self.assertEqual(_.join(['a', 'b', 'c'], '~'), 'a~b~c')

  def test_last(self):
    self.assertEqual(_.last([1, 2, 3]), 3)
  
  def test_lastIndexOf(self):
    self.assertEqual(_.lastIndexOf([1, 2, 1, 2], 2), 3)
    self.assertEqual(_.lastIndexOf([1, 2, 1, 2], 2, 2), 1)

  def test_nth(self):
    self.assertEqual(_.nth(['a', 'b', 'c', 'd'], 1), 'b')

  def test_pull(self):
    array = ['a', 'b', 'c', 'a', 'b', 'c']
    _.pull(array, 'a', 'c')
    self.assertEqual(array, ['b', 'b'])
  
  def test_pullAll(self):
    array = ['a', 'b', 'c', 'a', 'b', 'c']
    _.pullAll(array, ['a', 'c'])
    self.assertEqual(array, ['b', 'b'])

  def test_pullAt(self):
    array = ['a', 'b', 'c', 'd']
    pulled = _.pullAt(array, [1, 3])
    self.assertEqual(array, ['a', 'c'])
    self.assertEqual(pulled, ['b', 'd'])

  def test_remove(self):
    array = [1, 2, 3, 4]
    evens = _.remove(array, lambda n: n % 2 == 0)
    self.assertEqual(evens, [2, 4])
    self.assertEqual(array, [1, 3])

  def test_reverse(self):
    self.assertEqual(_.reverse([1, 2, 3]), [3, 2, 1])
    
  def test_slice(self):
    self.assertEqual(_.slice([1, 2, 3, 4], 1), [2, 3, 4])
    self.assertEqual(_.slice([1, 2, 3, 4], 1, 3), [2, 3])
  
  def test_sortedIndex(self):
    self.assertEqual(_.sortedIndex([30, 50], 40), 1)

  def test_sortedLastIndex(self):
    self.assertEqual(_.sortedLastIndex([4, 5, 5, 5, 6], 5), 4)

  def test_sortedUniq(self):
    self.assertEqual(_.sortedUniq([1, 1, 2]), [1, 2])
 
  def test_tail(self):
    self.assertEqual(_.tail([1, 2, 3]), [2, 3])
  
  def test_take(self):
    self.assertEqual(_.take([1, 2, 3]), [1])
    self.assertEqual(_.take([1, 2, 3], 2), [1, 2])
    self.assertEqual(_.take([1, 2, 3], 5), [1, 2, 3])
    self.assertEqual(_.take([1, 2, 3], 0), [])

  def test_takeRight(self):
    self.assertEqual(_.takeRight([1, 2, 3]), [3])
    self.assertEqual(_.takeRight([1, 2, 3], 2), [2, 3])
    self.assertEqual(_.takeRight([1, 2, 3], 5), [1, 2, 3])
    self.assertEqual(_.takeRight([1, 2, 3], 0), [])

  def test_takeRightWhile(self):
    users = [
      { 'user': 'barney',  'active': False },
      { 'user': 'fred',    'active': False },
      { 'user': 'pebbles', 'active': True }
    ]
    _.takeWhile(users, lambda o: not o['active'])
    self.assertEqual(users, [
      { 'user': 'barney',  'active': False },
      { 'user': 'fred',    'active': False },
    ])
  
  def test_takeWhile(self):
    users = [
      { 'user': 'barney',  'active': False },
      { 'user': 'fred',    'active': False },
      { 'user': 'pebbles', 'active': True }
    ]
    _.takeWhile(users, lambda o: not o['active'])
    self.assertEqual(users, [
      { 'user': 'barney',  'active': False },
      { 'user': 'fred',    'active': False },
    ])


  def test_union(self):
    self.assertEqual(_.union([2], [1, 2]), [2, 1])

  def test_uniq(self):
    self.assertEqual(_.uniq([2, 1, 2]), [1, 2])

  def test_unzip(self):
    self.assertEqual(_.unzip([['a', 1, True], ['b', 2, False]]), [['a', 'b'], [1, 2], [True, False]])

  def test_unzipWith(self):
    self.assertEqual(_.unzipWith([[1, 10, 100], [2, 20, 200]], _.add), [3, 30, 300])
  
  def test_without(self):
    self.assertEqual(_.without([2, 1, 2, 3], 1, 2), [3])
  
  def test_xor(self):
    self.assertEqual(_.xor([2, 1], [2, 3]), [1, 3])

  def test_zip(self):
    grouped = _.zip(["a", "b", None], [1, 2], [True, False], [])
    expected = [
      ["a", 1, True, None],
      ["b", 2, False, None],
      [None, None, None, None]
    ]
    self.assertEqual(grouped, expected)
  
  def test_zipObject(self):
    self.assertEqual(_.zipObject(['a', 'b'], [1, 2]), { 'a': 1, 'b': 2 })

class TestCollectionMethods(unittest.TestCase):
  def test_countBy(self):
    self.assertEqual(_.countBy([6.1, 4.2, 6.3], _.floor), { 4: 1, 6: 2 })

  def test_every(self):
    self.assertTrue(_.every([4, 6], lambda n: n > 2))
    self.assertFalse(_.every([4, 6], lambda n: n > 4))

  def test_filter(self):
    self.assertEqual(_.filter([4, 6], lambda n: n % 3 == 0), [6])

  def test_find(self):
    users = [
      { 'user': 'barney',  'age': 36, 'active': True },
      { 'user': 'fred',    'age': 40, 'active': False },
      { 'user': 'pebbles', 'age': 1,  'active': True }
    ]
    self.assertEqual(_.find(users, lambda u: u['age'] < 40), { 'user': 'barney',  'age': 36, 'active': True })
    self.assertEqual(_.find(users, lambda u: u['active']), { 'user': 'barney',  'age': 36, 'active': True })
    self.assertEqual(_.find(users, lambda u: u['age'] > 40), None)
  
  def test_findLast(self):
    self.assertEqual(_.findLast([1, 2, 3, 4], lambda n: n % 2 == 1), 3)
  
  def test_flatMap(self):
    self.assertEqual(_.flatMap([1, 2], lambda n: [n, n]), [1, 1, 2, 2])
  
  def test_flatMapDeep(self):
    self.assertEqual(_.flatMapDeep([1, 2], lambda n: [[[n, n]]]), [1, 1, 2, 2])

  def test_flatMapDepth(self):
    self.assertEqual(_.flatMapDepth([1, 2], lambda n: [[[n, n]]], 2), [[1, 1], [2, 2]])

  def test_forEach(self):
    _.forEach([1, 2], lambda n: print('n', n))

  def test_forEachRight(self):
    _.forEachRight([1, 2], lambda n: print('n', n))

  def test_groupBy(self):
    self.assertEqual(_.groupBy([6.1, 4.2, 6.3], _.floor), { '4': [4.2], '6': [6.1, 6.3] })

  def test_includes(self):
    self.assertTrue(_.includes([1, 2, 3], 1))
    self.assertFalse(_.includes([1, 2, 3], 1, 2))

  def test_invokeMap(self):
    self.assertEqual(_.invokeMap([[5, 1, 7], [3, 2, 1]], sorted), [[1, 5, 7], [1, 2, 3]])
    self.assertEqual(_.invokeMap([123, 456], _.split, ''), [['1', '2', '3'], ['4', '5', '6']])

  def test_keyBy(self):
    array = [
      { 'dir': 'left', 'code': 97 },
      { 'dir': 'right', 'code': 100 }
    ]
    obj = _.keyBy(array, lambda i: i['dir'])
    self.assertEqual(obj, { 'left': { 'dir': 'left', 'code': 97 }, 'right': { 'dir': 'right', 'code': 100 } })

  def test_map(self):
    self.assertEqual(_.map([4, 8], lambda n: n * n), [16, 64])

  def test_partition(self):
    users = [
      { 'user': 'barney',  'age': 36, 'active': False },
      { 'user': 'fred',    'age': 40, 'active': True },
      { 'user': 'pebbles', 'age': 1,  'active': False }
    ]
    self.assertEqual(_.partition(users, lambda o: o['active']), [
      [{ 'user': 'fred',    'age': 40, 'active': True }],
      [{ 'user': 'barney',  'age': 36, 'active': False }, { 'user': 'pebbles', 'age': 1,  'active': False }]
    ])
  
  def test_reduce(self):
    self.assertEqual(_.reduce([1, 2], lambda sum, n: sum + n, 0), 3)
    def iteratee(result, value, key):
      if str(value) in result:
        result[str(value)].append(key)
      else:
        result[str(value)] = [key]
      return result
    self.assertEqual(_.reduce({ 'a': 1, 'b': 2, 'c': 1 }, iteratee, {}), { '1': ['a', 'c'], '2': ['b'] })

  def test_reduceRight(self):
    array = [[0, 1], [2, 3], [4, 5]]
    self.assertEqual(_.reduceRight(array, lambda flattened, other: _.concat(flattened, other), []), [4, 5, 2, 3, 0, 1])

  def test_reject(self):
    users = [
      { 'user': 'barney', 'age': 36, 'active': False },
      { 'user': 'fred',   'age': 40, 'active': True }
    ]
    self.assertEqual(_.reject(users, lambda o: not o['active']), [{ 'user': 'fred',   'age': 40, 'active': True }])

  def test_sample(self):
    array = [1, 2, 3, 4]
    sample = _.sample(array)
    self.assertTrue(sample in array)

  def test_sampleSize(self):
    samples = _.sampleSize([1, 2, 3], 2)
    print('samples', samples)
    self.assertEqual(len(samples), 2)

  def test_shuffle(self):
    array = [1, 2, 3, 4]
    _.shuffle(array)
    self.assertEqual(len(array), len(array))

  def test_size(self):
    self.assertEqual(_.size('pebbles'), 7)
    self.assertEqual(_.size([1, 2, 3]), 3)
    self.assertEqual(_.size({ 'a': 1, 'b': 2 }), 2)

  def test_some(self):
    self.assertTrue(_.some([4, 6], lambda n: n > 2))
    self.assertFalse(_.some([4, 6], lambda n: n > 8))
  
  def test_sortBy(self):
    users = [
      { 'user': 'fred',   'age': 48 },
      { 'user': 'barney', 'age': 36 },
      { 'user': 'fred',   'age': 40 },
      { 'user': 'barney', 'age': 34 }
    ]
    self.assertEqual(_.sortBy(users, 'user'), [
      { 'user': 'barney', 'age': 36 },
      { 'user': 'barney', 'age': 34 },
      { 'user': 'fred',   'age': 48 },
      { 'user': 'fred',   'age': 40 }
    ])

class TestDateMethods(unittest.TestCase):
  def test_now(self):
    now = _.now()
    print(now)
    self.assertIsInstance(_.now(), int)
  
class TestFunctionMethods(unittest.TestCase):
  def test_debouce(self):
    def func():
      print('wait for 1 seconds')
    _.debounce(func, 1)
  
  def test_delay(self):
    def func(text):
      print(text)
    _.delay(func, 1, "wait for 1 seconds")

class TestLangMethods(unittest.TestCase):
  def test_castArray(self):
    self.assertEqual(_.castArray(1), [1])
    self.assertEqual(_.castArray({ 'a': 1 }), [{ 'a': 1 }])
    self.assertEqual(_.castArray('abc'), ['abc'])
    self.assertEqual(_.castArray(None), [None])

  def test_conformsTo(self):
    object = { 'a': 1, 'b': 2 }
    self.assertTrue(_.conformsTo(object, { 'b': lambda n: n > 1 }))

  def test_clone(self):
    objects = [{ 'a': 1 }, { 'b': 2 }]
    shallow = _.clone(objects)
    self.assertEqual(objects[0], shallow[0])

  def test_cloneDeep(self):
    objects = [{ 'a': 1 }, { 'b': 2 }]
    deep = _.cloneDeep(objects)
    self.assertEqual(objects[0], deep[0])

  def test_cloneDeepWith(self):
    objects = [{ 'a': 1 }, { 'b': 2 }]
    deepValue = _.cloneDeepWith(objects, lambda o: o[0])
    self.assertEqual(deepValue, { 'a': 1 })

  def test_cloneWith(self):
    objects = [{ 'a': 1 }, { 'b': 2 }]
    deepValue = _.cloneWith(objects, lambda o: o[0])
    self.assertEqual(deepValue, { 'a': 1 })

  def test_eq(self):
    self.assertTrue(_.eq({ 'a': 1 }, { 'a': 1 }))
    self.assertTrue(_.eq('a', 'a'))
    self.assertFalse(_.eq({ 'a': 1 }, 'a'))
    self.assertFalse(_.eq('a', 1))

  def test_gt(self):
    self.assertTrue(_.gt(3, 1))
    self.assertFalse(_.gt(3, 3))
    self.assertFalse(_.gt(1, 3))
  
  def test_gte(self):
    self.assertTrue(_.gte(3, 1))
    self.assertTrue(_.gte(3, 3))
    self.assertFalse(_.gte(1, 3))
  
  def test_isArray(self):
    self.assertTrue(_.isArray([1, 2, 3]))
    self.assertFalse(_.isArray(123))

  def test_isArrayLike(self):
    self.assertTrue(_.isArrayLike([1, 2, 3]))
    self.assertTrue(_.isArrayLike('abc'))
    self.assertFalse(_.isArrayLike(_.noop))

  def test_isArrayLikeObject(self):
    self.assertTrue(_.isArrayLikeObject([1, 2, 3]))
    self.assertFalse(_.isArrayLikeObject('abc'))
    self.assertFalse(_.isArrayLikeObject(_.noop))

  def test_isBoolean(self):
    self.assertTrue(_.isBoolean(True))
    self.assertTrue(_.isBoolean(False))
    self.assertFalse(_.isBoolean(None))

  def test_isEmpty(self):
    self.assertTrue(_.isEmpty(None))
    self.assertTrue(_.isEmpty(True))
    self.assertTrue(_.isEmpty(1))
    self.assertFalse(_.isEmpty([1, 2, 3]))
    self.assertTrue(_.isEmpty([]))
    self.assertFalse(_.isEmpty({ 'a': 1 }))
    self.assertTrue(_.isEmpty({}))

  def test_isEqual(self):
    self.assertTrue(_.isEqual({ 'a': 1 }, { 'a': 1 }))

  def test_isEqualWith(self):
    object = { 'a': 1 }
    other = { 'a': 3 }
    self.assertTrue(_.isEqualWith(object, other, lambda o: o['a'] % 2 == 1))

  def test_isFinite(self):
    self.assertTrue(_.isFinite(3))
    self.assertFalse(_.isFinite('3'))
    self.assertFalse(_.isFinite(float('-inf')))

  def test_isFunction(self):
    def a():
      return
    self.assertTrue(_.isFunction(a))
    self.assertTrue(_.isFunction(lambda a: a))

  def test_isInteger(self):
    self.assertTrue(_.isInteger(3))
    self.assertFalse(_.isInteger('3'))
  
  def test_isLength(self):
    self.assertTrue(_.isLength(3))
    self.assertFalse(_.isLength('3'))

  def test_isMatch(self):
    obj = { 'a': 1, 'b': 2 }
    self.assertTrue(_.isMatch(obj, { 'b': 2 }))
    self.assertFalse(_.isMatch(obj, { 'b': 1 }))
  
  def test_isMatchWith(self):
    obj = { 'a': 1, 'b': 2 }
    self.assertTrue(_.isMatchWith(obj, { 'b': 4 }, lambda value: value % 2 == 0))
    self.assertFalse(_.isMatchWith(obj, { 'b': 1 }, lambda value: value % 2 == 0))

  def test_isNil(self):
    self.assertTrue(_.isNil(None))
  
  def test_isNull(self):
    self.assertTrue(_.isNull(None))
  
  def test_isNumber(self):
    self.assertTrue(_.isNumber(3))
    self.assertFalse(_.isNumber('3'))
    self.assertTrue(_.isNumber(float('-inf')))

  def test_isObject(self):
    self.assertTrue(_.isObject({}))
    self.assertFalse(_.isObject(None))

  def test_isObjectLike(self):
    self.assertTrue(_.isObjectLike({}))
    self.assertTrue(_.isObjectLike([]))
    self.assertFalse(_.isObjectLike(None))

  def test_isSafeInteger(self):
    self.assertTrue(_.isSafeInteger(3))
    self.assertFalse(_.isSafeInteger('3'))
    self.assertFalse(_.isSafeInteger(float('inf')))

  def test_isSet(self):
    self.assertTrue(_.isSet(set([1, 2, 3])))

  def test_isString(self):
    self.assertTrue(_.isString('abc'))
    self.assertFalse(_.isString(123))

  def test_isUndefined(self):
    self.assertTrue(_.isUndefined(None))
  
  def test_lt(self):
    self.assertTrue(_.lt(1, 3))
    self.assertFalse(_.lt(3, 3))
    self.assertFalse(_.lt(3, 1))
  
  def test_lte(self):
    self.assertTrue(_.lte(1, 3))
    self.assertTrue(_.lte(3, 3))
    self.assertFalse(_.lte(3, 1))

  def test_toArray(self):
    self.assertEqual(_.toArray({ 'a': 1, 'b': 2 }), [1, 2])
    self.assertEqual(_.toArray('abc'), ['a', 'b', 'c'])
    self.assertEqual(_.toArray(1), [])
    self.assertEqual(_.toArray(None), [])

  def test_toInteger(self):
    self.assertEqual(_.toInteger(3.2), 3)
    self.assertEqual(_.toInteger('3.2'), 3)

  def test_toLength(self):
    self.assertEqual(_.toLength(3.2), 3)
    self.assertEqual(_.toLength('3.2'), 3)

  def test_toNumber(self):
    self.assertEqual(_.toNumber(3.2), 3.2)
    self.assertEqual(_.toNumber('3.2'), 3.2)
  
  def test_toSafeInteger(self):
    self.assertEqual(_.toSafeInteger(3.2), 3)
    self.assertEqual(_.toSafeInteger(float('inf')), 9223372036854775807)
    self.assertEqual(_.toSafeInteger(float('-inf')), -9223372036854775808)

  def test_toString(self):
    self.assertIsInstance(_.toString(-9), str)

class TestMathMethods(unittest.TestCase):
  def test_add(self):
    self.assertEqual(_.add(6, 4), 10)

  def test_ceil(self):
    self.assertEqual(_.ceil(4.006), 5)

  def test_divide(self):
    self.assertEqual(_.divide(6, 4), 1.5)

  def test_floor(self):
    self.assertEqual(_.floor(4.006), 4)

  def test_max(self):
    self.assertEqual(_.max([4, 2, 8, 6]), 8)
  
  def test_maxBy(self):
    self.assertEqual(_.maxBy([{ 'n': 1 }, { 'n': 2 }], 'n'), 2)

  def test_mean(self):
    self.assertEqual(_.mean([4, 2, 8, 6]), 5)

  def test_meanBy(self):
    self.assertEqual(_.meanBy([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], 'n'), 5)

  def test_min(self):
    self.assertEqual(_.min([4, 2, 8, 6]), 2)
  
  def test_minBy(self):
    self.assertEqual(_.minBy([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], 'n'), 2)

  def test_multiply(self):
    self.assertEqual(_.multiply(6, 4), 24)

  def test_roundNumber(self):
    self.assertEqual(_.roundNumber(4.006, 2), 4.01)

  def test_subtract(self):
    self.assertEqual(_.subtract(6, 4), 2)

  def test_sum(self):
    self.assertEqual(_.sum([4, 2, 8, 6]), 20)

  def test_sumBy(self):
    self.assertEqual(_.sumBy([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], 'n'), 20)

class TestNumberMethods(unittest.TestCase):
  def test_clamp(self):
    self.assertEqual(_.clamp(-10, -5, 5), -5)
    self.assertEqual(_.clamp(10, -5, 5), 5)

  def test_inRange(self):
    self.assertTrue(_.inRange(3, 2, 4))
    self.assertTrue(_.inRange(4, 8))
    self.assertFalse(_.inRange(4, 2))
    self.assertFalse(_.inRange(2, 2))
    self.assertTrue(_.inRange(1.2, 2))
    self.assertFalse(_.inRange(5.4, 4))
    self.assertFalse(_.inRange(-3, -2, -6))

  def test_random(self):
    random1 = _.random(5)
    self.assertTrue(0 <= random1 and random1 <= 5)
    random2 = _.random(5, 10)
    self.assertTrue(5 <= random2 and random2 <= 10)

class TestObjectMethods(unittest.TestCase):
  def test_assign(self):
    self.assertEqual(_.assign({ 'a': 0 }, { 'a': 1 }, { 'b': 1 }), { 'a': 1, 'b': 1 })

  def test_at(self):
    obj = { 'a': { 'b': { 'c': 3 }, 'd': 4 } }
    self.assertEqual(_.at(obj, ['a.b.c', 'a.d']), [3, 4])

  def test_defaults(self):
    self.assertEqual(_.defaults({ 'a': 1 }, { 'b': 2 }, { 'a': 3 }), { 'a': 1, 'b': 2 })

  def test_findKey(self):
    users = {
      'barney':  { 'age': 36, 'active': True },
      'fred':    { 'age': 40, 'active': False },
      'pebbles': { 'age': 1,  'active': True }
    }
    self.assertEqual(_.findKey(users, lambda u: u['age'] < 40), 'barney')
    self.assertEqual(_.findKey(users, lambda u: u['age'] == 1 and u['active']), 'pebbles')
    self.assertEqual(_.findKey(users, lambda u: not u['active']), 'fred')
    self.assertEqual(_.findKey(users, lambda u: u['active']), 'barney')

  def test_forIn(self):
    object = {
      'a': 1,
      'b': 2,
      'c': 3
    }
    _.forIn(object, lambda value, key: print(key, value))

  def test_forInRight(self):
    object = {
      'a': 1,
      'b': 2,
      'c': 3
    }
    _.forInRight(object, lambda value, key: print(key, value))

  def test_forOwn(self):
    object = {
      'a': 1,
      'b': 2,
      'c': 3
    }
    _.forOwn(object, lambda value, key: print(key, value))

  def test_forOwnRight(self):
    object = {
      'a': 1,
      'b': 2,
      'c': 3
    }
    _.forOwnRight(object, lambda value, key: print(key, value))

  def test_findLastKey(self):
    users = {
      'barney':  { 'age': 36, 'active': True },
      'fred':    { 'age': 40, 'active': False },
      'pebbles': { 'age': 1,  'active': True }
    }
    self.assertEqual(_.findLastKey(users, lambda u: u['age'] < 40), 'pebbles')
    self.assertEqual(_.findLastKey(users, lambda u: u['age'] == 36 and u['active']), 'barney')
    self.assertEqual(_.findLastKey(users, lambda u: not u['active']), 'fred')
    self.assertEqual(_.findLastKey(users, lambda u: u['active']), 'pebbles')

  def test_functions(self):
    object = {
      'a': _.constant('a'),
      'b': _.constant('b')
    }
    self.assertEqual(_.functions(object), ['a', 'b'])
 
  def test_functionsIn(self):
    object = {
      'a': _.constant('a'),
      'b': _.constant('b'),
      'c': _.constant('c')
    }
    self.assertEqual(_.functionsIn(object), ['a', 'b', 'c'])

  def test_get(self):
    obj = { 'a': { 'b': 1 } }
    self.assertEqual(_.get(obj, 'a.b'), 1)
    self.assertEqual(_.get(obj, 'a.b.c'), None)
  
  def test_has(self):
    object = { 'a': { 'b': 2 } }
    self.assertTrue(_.has(object, 'a'))
    self.assertTrue(_.has(object, 'a.b'))
    self.assertFalse(_.has(object, 'c'))

  def test_invert(self):
    self.assertEqual(_.invert({ 'a': 1, 'b': 2, 'c': 1 }), { '1': 'c', '2': 'b' })
  
  def test_invertBy(self):
    self.assertEqual(_.invertBy({ 'a': 1, 'b': 2, 'c': 1 }), { '1': ['a', 'c'], '2': ['b'] })

  def test_keys(self):
    self.assertEqual(_.keys({ 'a': 1, 'b': 2 }), ['a', 'b'])

  def test_keysIn(self):
    self.assertEqual(_.keys({ 'a': 1, 'b': 2, 'c': 3 }), ['a', 'b', 'c'])

  def test_mapKeys(self):
    self.assertEqual(_.mapKeys({ 'a': 1, 'b': 2 }, lambda value, key: str(key) + str(value)), { 'a1': 1, 'b2': 2 })

  def test_mapValues(self):
    users = {
      'fred':    { 'user': 'fred',    'age': 40 },
      'pebbles': { 'user': 'pebbles', 'age': 1 }
    }
    _.mapValues(users, lambda o: o['age'])
    self.assertEqual(users, { 'fred': 40, 'pebbles': 1 })

  def test_omit(self):
    object = { 'a': 1, 'b': '2', 'c': 3 }
    self.assertEqual(_.omit(object, ['a', 'c']), { 'b': '2' })

  def test_omitBy(self):
    object = { 'a': 1, 'b': '2', 'c': 3 }
    self.assertEqual(_.omitBy(object, _.isNumber), { 'b': '2' })

  def test_pick(self):
    obj = { 'a': 1, 'b': '2', 'c': 3 }
    self.assertEqual(_.pick(obj, ['a', 'c']), { 'a': 1, 'c': 3 })

  def test_pickBy(self):
    object = { 'a': 1, 'b': '2', 'c': 3 }
    self.assertEqual(_.pickBy(object, _.isNumber), { 'a': 1, 'c': 3 })

  def test_result(self):
    obj = { 'a': { 'b': { 'c1': 3, 'c2': _.constant(4) } } }
    self.assertEqual(_.result(obj, 'a.b.c1'), 3)
    self.assertEqual(_.result(obj, 'a.b.c2'), 4)

  def test_setObject(self):
    obj = { 'a': { 'b': {'c': 0 }}}
    self.assertEqual(_.setObject(obj, 'a.b.c', 1), { 'a': { 'b': { 'c': 1 }}})

  def test_toPairs(self):
    obj = { 'a': 1, 'b': 2 }
    self.assertEqual(_.toPairs(obj), [['a', 1], ['b', 2]])

  def test_toPairsIn(self):
    obj = { 'a': 1, 'b': 2, 'c': 3 }
    self.assertEqual(_.toPairs(obj), [['a', 1], ['b', 2], ['c', 3]])

  def test_update(self):
    obj = { 'a': { 'b': { 'c': 3 } } }
    _.update(obj, 'a.b.c', lambda n: n * n)
    self.assertEqual(obj, { 'a': { 'b': { 'c': 9 } } })

  def test_values(self):
    obj = { 'a': 1, 'b': 2 }
    self.assertEqual(_.values(obj), [1, 2])

  def test_valuesIn(self):
    obj = { 'a': 1, 'b': 2, 'c': 3 }
    self.assertEqual(_.valuesIn(obj), [1, 2, 3])

class TestStringMethods(unittest.TestCase):
  def test_camelCase(self):
    self.assertEqual(_.camelCase('Foo bar'), 'fooBar')

  def test_capitalize(self):
    self.assertEqual(_.capitalize('FOO'), 'Foo')

  def test_endsWith(self):
    self.assertTrue(_.endsWith('abc', 'c'))
    self.assertFalse(_.endsWith('abc', 'b'))
    self.assertTrue(_.endsWith('abc', 'b', 2))
  
  def test_kebabCase(self):
    self.assertEqual(_.kebabCase('Foo Bar'), 'foo-bar')

  def test_lowerCase(self):
    self.assertEqual(_.lowerCase('--Foo--Bar--'), 'foo bar')
    self.assertEqual(_.lowerCase('__Foo__Bar__'), 'foo bar')

  def test_lowerFirst(self):
    self.assertEqual(_.lowerFirst('Fred'), 'fred')
    self.assertEqual(_.lowerFirst('FRED'), 'fRED')

  def test_pad(self):
    self.assertEqual(_.pad('abc', 8), '  abc   ')
    self.assertEqual(_.pad('abc', 8, '_-'), '_-abc_-_')
    self.assertEqual(_.pad('abc', 3), 'abc')

  def test_padEnd(self):
    self.assertEqual(_.padEnd('abc', 6), 'abc   ')
    self.assertEqual(_.padEnd('abc', 6, '_-'), 'abc_-_')
    self.assertEqual(_.padEnd('abc', 3), 'abc')

  def test_padStart(self):
    self.assertEqual(_.padStart('abc', 6), '   abc')
    self.assertEqual(_.padStart('abc', 6, '_-'), '_-_abc')
    self.assertEqual(_.padStart('abc', 3), 'abc')

  def test_parseInt(self):
    self.assertEqual(_.parseInt('08'), 8)

  def test_repeat(self):
    self.assertEqual(_.repeat('*', 3), '***')

  def test_replace(self):
    self.assertEqual(_.replace('placeholder', 'placeholder', 'test'), 'test')

  def test_snakeCase(self):
    self.assertEqual(_.snakeCase('Foo Bar'), 'foo_bar')

  def test_split(self):
    self.assertEqual(_.split('a-b-c', '-'), ['a', 'b', 'c'])
    self.assertEqual(_.split('a-b-c', '-', 2), ['a', 'b'])

  def test_startCase(self):
    self.assertEqual(_.startCase('--foo--bar--'), 'Foo Bar')
    self.assertEqual(_.startCase('__foo__bar__'), 'Foo Bar')

  def test_startsWith(self):
    self.assertTrue(_.startsWith('test', 't'))
    self.assertFalse(_.startsWith('test', 'e'))
    self.assertTrue(_.startsWith('test', 'e', 1))

  def test_toLower(self):
    self.assertEqual(_.toLower('TEST'), 'test')

  def test_toUpper(self):
    self.assertEqual(_.toUpper('test'), 'TEST')

  def test_trim(self):
    self.assertEqual(_.trim('   abc   '), 'abc')

  def test_trimEnd(self):
    self.assertEqual(_.trimEnd('   abc   '), '   abc')

  def test_trimStart(self):
    self.assertEqual(_.trimStart('   abc   '), 'abc   ')

  def test_truncate(self):
    self.assertEqual(_.truncate('hi-diddly-ho there, neighborino'), 'hi-diddly-ho there, neighbo ...')
  
  def test_upperCase(self):
    self.assertEqual(_.upperCase('--Foo--Bar--'), 'FOO BAR')
    self.assertEqual(_.upperCase('__Foo__Bar__'), 'FOO BAR')

  def test_upperFirst(self):
    self.assertEqual(_.upperFirst('tEST'), 'Test')

  def test_words(self):
    self.assertEqual(_.words('fred, barney, & pebbles'), ['fred', 'barney', 'pebbles'])

class TestUtilMethods(unittest.TestCase):
  def test_constant(self):
    self.assertEqual(_.times(2, _.constant({ 'a': 1 })), [{ 'a': 1 }, { 'a': 1 }])

  def test_defaultTo(self):
    self.assertEqual(_.defaultTo(1, 10), 1)
    self.assertEqual(_.defaultTo(None, 10), 10)
  
  def test_identity(self):
    obj = { 'a': 1 }
    self.assertEqual(_.identity(obj), obj)
    self.assertEqual(_.identity(123), 123)
    self.assertEqual(_.identity(obj, 123), obj)

  def test_noop(self):
    self.assertEqual(_.noop(), None)

  def test_rangeArray(self):
    self.assertEqual(_.rangeArray(4), [0, 1, 2, 3])
    self.assertEqual(_.rangeArray(1, 5), [1, 2, 3, 4])
    self.assertEqual(_.rangeArray(0, 20, 5), [0, 5, 10, 15])

  def test_rangeRight(self):
    self.assertEqual(_.rangeRight(4), [3, 2, 1, 0])
    self.assertEqual(_.rangeRight(1, 5), [4, 3, 2, 1])
    self.assertEqual(_.rangeRight(0, 20, 5), [15, 10, 5, 0])

  def test_stubArray(self):
    self.assertEqual(_.stubArray(), [])

  def test_stubFalse(self):
    self.assertFalse(_.stubFalse())

  def test_stubObject(self):
    self.assertEqual(_.stubObject(), {})

  def test_stubString(self):
    self.assertEqual(_.stubString(), '')

  def test_stubTrue(self):
    self.assertTrue(_.stubTrue())

  def test_times(self):
    self.assertEqual(_.times(3), [0, 1, 2])
    self.assertEqual(_.times(4, _.constant(0)), [0, 0, 0, 0])

  def test_toPath(self):
    self.assertEqual(_.toPath('a.b.c'), ['a', 'b', 'c'])
    self.assertEqual(_.toPath('a[0]b.c'), ['a', '0', 'b', 'c'])

  def test_uniqueId(self):
    uniqueId = _.uniqueId()
    print(uniqueId)

if __name__ == '__main__':
  unittest.main()
