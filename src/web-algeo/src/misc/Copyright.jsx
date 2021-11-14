import { Text } from '@chakra-ui/layout'
import * as React from 'react'

export const Copyright = (props) => (
  <Text fontSize="sm" {...props} color="#01CC90">
    &copy; {new Date().getFullYear()} Pemuja Hidayah-Mu, diniatkan dengan hati, dikerjakan dengan hati.
  </Text>
)