const encode = function (input) {
  var TABLE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

  input = String(input)
  if (/[^\0-\xFF]/.test(input)) {
    console.error('The string to be encoded contains characters outside of the ' + 'Latin1 range.')
  }
  var padding = input.length % 3
  var output = ''
  var position = -1
  var a
  var b
  var c
  var buffer
  var length = input.length - padding

  while (++position < length) {
    a = input.charCodeAt(position) << 16
    b = input.charCodeAt(++position) << 8
    c = input.charCodeAt(++position)
    buffer = a + b + c
    // Turn the 24 bits into four chunks of 6 bits each, and append the
    // matching character for each of them to the output.
    output += (
      TABLE.charAt(buffer >> 18 & 0x3F) +
      TABLE.charAt(buffer >> 12 & 0x3F) +
      TABLE.charAt(buffer >> 6 & 0x3F) +
      TABLE.charAt(buffer & 0x3F)
    )
  }

  if (padding === 2) {
    a = input.charCodeAt(position) << 8
    b = input.charCodeAt(++position)
    buffer = a + b
    output += (
      TABLE.charAt(buffer >> 10) +
       TABLE.charAt((buffer >> 4) & 0x3F) +
       TABLE.charAt((buffer << 2) & 0x3F) +
       '='
    )
  } else if (padding === 1) {
    buffer = input.charCodeAt(position)
    output += (
      TABLE.charAt(buffer >> 2) +
      TABLE.charAt((buffer << 4) & 0x3F) +
      '=='
    )
  }

  return output
}

const base64 = {
  encode
}

export default base64
