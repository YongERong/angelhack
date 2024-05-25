'use client'

import { ChakraProvider, ThemeProvider} from '@chakra-ui/react'
import theme  from './theme'

export function Providers({ children }) {
  return <ChakraProvider theme={theme}><ThemeProvider theme={theme}>{children}</ThemeProvider></ChakraProvider>
}